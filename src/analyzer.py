"""
Pashify Password Analyzer Engine
Combines ML inference, multi-dimensional security scoring (0-100),
password characteristics breakdown, and recommendation generation.
"""

import pickle
import re
import os
import streamlit as st
from scipy.sparse import hstack

from src.config import MODEL_PATH, VECTORIZER_PATH, MAX_PASSWORD_LENGTH
from src.entropy import calculate_entropy, estimate_crack_time, get_entropy_explanation
from src.breach_checker import check_local_breach, check_pwned_api

COMMON_PATTERNS = [
    "123456", "password", "123456789", "qwerty", "12345678", "111111",
    "1234567", "dragon", "12345", "welcome", "administrator", "admin",
    "iloveyou", "sunshine", "monkey", "charlie", "password123"
]

@st.cache_resource
def load_ml_components():
    """Loads and caches the optimized ML model and TF-IDF vectorizer."""
    try:
        if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
            model = pickle.load(open(MODEL_PATH, "rb"))
            vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))
            return model, vectorizer
        return None, None
    except Exception as e:
        st.error(f"⚠️ Unable to load ML classifier models: {e}")
        return None, None


def transform_password(password: str, vectorizer):
    """Transforms input string into character n-gram + length sparse feature matrix."""
    if not vectorizer or not password:
        return None
    vec = vectorizer.transform([password])
    length = [[len(password)]]
    return hstack([vec, length])


def analyze_password(password: str) -> dict:
    """
    Executes a complete 360-degree security audit on a password string.
    
    Returns structured analysis dictionary:
    - password_length
    - strength_class (WEAK, MEDIUM, STRONG)
    - ml_prediction_code (0, 1, 2)
    - security_score (0-100)
    - entropy (bits)
    - entropy_explanation
    - crack_times (dict)
    - breach_status (is_breached, breach_count, is_local)
    - characteristics (uppercase, lowercase, numbers, symbols, unique_ratio)
    - recommendations (list of strings)
    """
    if not password:
        return {}

    # Safety Capping
    if len(password) > MAX_PASSWORD_LENGTH:
        password = password[:MAX_PASSWORD_LENGTH]

    model, vectorizer = load_ml_components()

    # 1. ML Prediction Inference
    ml_code = 0
    if model and vectorizer:
        try:
            vector = transform_password(password, vectorizer)
            if vector is not None:
                ml_code = int(model.predict(vector)[0])
        except Exception:
            ml_code = 0

    strength_map = {0: "WEAK", 1: "MEDIUM", 2: "STRONG"}
    strength_label = strength_map.get(ml_code, "WEAK")

    # 2. Entropy & Crack Speeds
    entropy = calculate_entropy(password)
    entropy_exp = get_entropy_explanation(entropy)
    crack_times = estimate_crack_time(entropy)

    # 3. Breach Intelligence
    is_local = check_local_breach(password)
    is_pwned, pwned_count = check_pwned_api(password)
    is_breached = is_local or is_pwned
    total_breach_count = pwned_count if pwned_count > 0 else (1 if is_local else 0)

    # 4. Characteristics Breakdown
    length = len(password)
    uppercase_count = len(re.findall(r"[A-Z]", password))
    lowercase_count = len(re.findall(r"[a-z]", password))
    digit_count = len(re.findall(r"\d", password))
    symbol_count = len(re.findall(r"[!@#$%^&*(),.?\":{}|<>\-_\[\]~`@#+\\=/;:]", password))
    unique_chars = len(set(password))
    diversity_ratio = round(unique_chars / length, 2) if length > 0 else 0

    # 5. Security Score Calculation (0 to 100)
    score = calculate_security_score(
        length=length,
        ml_code=ml_code,
        entropy=entropy,
        diversity_ratio=diversity_ratio,
        is_breached=is_breached,
        total_breach_count=total_breach_count,
        has_upper=uppercase_count > 0,
        has_lower=lowercase_count > 0,
        has_digit=digit_count > 0,
        has_symbol=symbol_count > 0,
        password_lower=password.lower()
    )

    # 6. Actionable Security Recommendations
    recommendations = generate_recommendations(
        password=password,
        length=length,
        is_breached=is_breached,
        total_breach_count=total_breach_count,
        has_upper=uppercase_count > 0,
        has_lower=lowercase_count > 0,
        has_digit=digit_count > 0,
        has_symbol=symbol_count > 0,
        diversity_ratio=diversity_ratio
    )

    return {
        "password_length": length,
        "strength_class": strength_label,
        "ml_code": ml_code,
        "security_score": score,
        "entropy": entropy,
        "entropy_explanation": entropy_exp,
        "crack_times": crack_times,
        "is_breached": is_breached,
        "breach_count": total_breach_count,
        "is_local_breach": is_local,
        "is_api_breach": is_pwned,
        "characteristics": {
            "length": length,
            "uppercase": uppercase_count,
            "lowercase": lowercase_count,
            "digits": digit_count,
            "symbols": symbol_count,
            "unique_chars": unique_chars,
            "diversity_ratio": diversity_ratio
        },
        "recommendations": recommendations
    }


def calculate_security_score(
    length: int,
    ml_code: int,
    entropy: float,
    diversity_ratio: float,
    is_breached: bool,
    total_breach_count: int,
    has_upper: bool,
    has_lower: bool,
    has_digit: bool,
    has_symbol: bool,
    password_lower: str
) -> int:
    """Calculates a robust 0-100 composite security rating."""
    score = 0.0

    # ML Baseline (0-30 points)
    ml_base = {0: 10.0, 1: 20.0, 2: 30.0}
    score += ml_base.get(ml_code, 10.0)

    # Entropy Weight (0-35 points)
    entropy_score = min(entropy / 128.0, 1.0) * 35.0
    score += entropy_score

    # Length Weight (0-20 points)
    if length >= 16:
        score += 20.0
    elif length >= 12:
        score += 15.0
    elif length >= 8:
        score += 8.0
    else:
        score += 2.0

    # Character Pool Diversity (0-15 points)
    pools_used = sum([has_upper, has_lower, has_digit, has_symbol])
    score += (pools_used / 4.0) * 15.0

    # Penalties
    # Common pattern / word penalty
    for pat in COMMON_PATTERNS:
        if pat in password_lower:
            score -= 25.0
            break

    # Repeating character penalty (e.g. "aaaaa", "11111")
    if diversity_ratio < 0.4 and length > 6:
        score -= 20.0

    # Breach penalty
    if is_breached:
        if total_breach_count > 1000:
            score = min(score, 15.0)  # Heavily cap score if widely leaked
        else:
            score = min(score, 30.0)

    return max(0, min(100, int(round(score))))


def generate_recommendations(
    password: str,
    length: int,
    is_breached: bool,
    total_breach_count: int,
    has_upper: bool,
    has_lower: bool,
    has_digit: bool,
    has_symbol: bool,
    diversity_ratio: float
) -> list[dict]:
    """Generates actionable security tips categorized by severity."""
    recs = []

    if is_breached:
        recs.append({
            "type": "CRITICAL",
            "icon": "🔴",
            "message": f"Password exposed in known data leaks ({total_breach_count:,} times). Replace immediately."
        })

    if length < 12:
        recs.append({
            "type": "WARNING",
            "icon": "⚠️",
            "message": f"Current length ({length} chars) is below recommended 12-character minimum for modern safety."
        })

    if not has_upper:
        recs.append({
            "type": "INFO",
            "icon": "💡",
            "message": "Add uppercase letters (A-Z) to expand character pool combinations."
        })

    if not has_lower:
        recs.append({
            "type": "INFO",
            "icon": "💡",
            "message": "Add lowercase letters (a-z) to increase state space entropy."
        })

    if not has_digit:
        recs.append({
            "type": "INFO",
            "icon": "💡",
            "message": "Include numerical digits (0-9) to disrupt dictionary pattern matching."
        })

    if not has_symbol:
        recs.append({
            "type": "INFO",
            "icon": "💡",
            "message": "Include special symbols (!@#$%) to defend against hybrid brute-force attacks."
        })

    if diversity_ratio < 0.5 and length > 6:
        recs.append({
            "type": "WARNING",
            "icon": "⚠️",
            "message": "High character repetition detected. Use more unique characters."
        })

    pwd_lower = password.lower()
    for pat in COMMON_PATTERNS:
        if pat in pwd_lower:
            recs.append({
                "type": "CRITICAL",
                "icon": "🔴",
                "message": f"Contains common dictionary sequence '{pat}'. Avoid predictable words."
            })
            break

    if not recs:
        recs.append({
            "type": "SUCCESS",
            "icon": "✅",
            "message": "Excellent password strength! Complies with modern cryptographic security standards."
        })

    return recs

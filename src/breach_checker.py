"""
Pashify Threat Intelligence & Breach Scanner
Implements SHA-1 K-Anonymity API integration with Have I Been Pwned
and local offline compromise list matching.
"""

import hashlib
import requests
import os
import streamlit as st
from src.config import BREACH_LIST_PATH, DEFAULT_API_TIMEOUT, MAX_PASSWORD_LENGTH

@st.cache_resource
def load_local_breached_set() -> set:
    """Loads and caches the local list of known leaked passwords."""
    breaches = set()
    if os.path.exists(BREACH_LIST_PATH):
        try:
            with open(BREACH_LIST_PATH, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    cleaned = line.strip()
                    if cleaned:
                        breaches.add(cleaned)
        except Exception as e:
            # Fallback gracefully
            pass
    return breaches


def check_local_breach(password: str) -> bool:
    """Checks if password exists in local offline threat list."""
    if not password:
        return False
    local_set = load_local_breached_set()
    return password in local_set


def check_pwned_api(password: str) -> tuple[bool, int]:
    """
    Queries HaveIBeenPwned API via SHA-1 K-Anonymity protocol.
    
    PRIVACY GUARANTEE:
    1. Raw password is NEVER sent over the internet or logged.
    2. Password is converted to SHA-1 hex hash locally.
    3. ONLY the first 5 characters (prefix) are sent to api.pwnedpasswords.com.
    4. The API returns candidate suffixes; matching occurs 100% locally.

    Returns:
        (is_breached: bool, breach_count: int)
    """
    if not password or len(password) > MAX_PASSWORD_LENGTH:
        return False, 0

    try:
        sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]

        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        headers = {"User-Agent": "Pashify-Password-Analyzer-v2"}
        
        response = requests.get(url, headers=headers, timeout=DEFAULT_API_TIMEOUT)
        
        if response.status_code != 200:
            return False, 0

        for line in response.text.splitlines():
            parts = line.split(":")
            if len(parts) == 2:
                h_suffix, count = parts[0].strip(), parts[1].strip()
                if h_suffix == suffix:
                    return True, int(count)

    except Exception:
        # Graceful failure on timeout or network offline
        return False, 0

    return False, 0


def get_privacy_statement() -> str:
    """Returns official Privacy & K-Anonymity guarantee text."""
    return (
        "🔒 PRIVACY GUARANTEE: Your complete password is NEVER sent to the breach database or logged. "
        "Pashify hashes your password locally using SHA-1 and transmits only the first 5 hex characters "
        "via the industry-standard k-Anonymity protocol. All comparison happens on your device."
    )

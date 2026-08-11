"""
Pashify Entropy & Crack Time Calculator
Computes Shannon / Pool Information Entropy and estimates brute-force crack time.
"""

import math
import re

def calculate_entropy(password: str) -> float:
    """
    Calculates password entropy in bits based on character pool size.
    Formula: Entropy = length * log2(pool_size)
    """
    if not password:
        return 0.0

    pool = 0
    if re.search(r"[a-z]", password):
        pool += 26
    if re.search(r"[A-Z]", password):
        pool += 26
    if re.search(r"\d", password):
        pool += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>\-_\[\]~`@#+\\=/;:]", password):
        pool += 33

    if pool == 0:
        pool = 95  # Standard printable ASCII fallback

    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)


def get_entropy_explanation(entropy: float) -> str:
    """Returns a simple, beginner-friendly explanation of the calculated entropy."""
    if entropy == 0:
        return "No entropy detected. Password is empty."
    elif entropy < 28:
        return "Very low entropy. Extremely vulnerable to basic automated automated guessing."
    elif entropy < 36:
        return "Low entropy. Typical target for rapid dictionary and hybrid brute-force attacks."
    elif entropy < 60:
        return "Moderate entropy. Provides standard defense against simple attacks, but vulnerable to dedicated GPU rigs."
    elif entropy < 80:
        return "High entropy. Strong cryptographic resistance against offline dictionary and brute-force attacks."
    else:
        return "Military-grade entropy. Practically impossible to crack using present computing hardware."


def estimate_crack_time(entropy: float) -> dict:
    """
    Estimates time required to brute-force a password based on entropy.
    Scenarios:
    1. Online Login (10 attempts/sec due to rate-limiting)
    2. GPU Cracking Rig (10 Billion attempts/sec)
    3. Supercomputer Cluster (100 Trillion attempts/sec)
    """
    if entropy <= 0:
        return {
            "Online Login Portal (10/sec)": "Instant",
            "GPU Cracking Rig (10B/sec)": "Instant",
            "Supercomputer Cluster (100T/sec)": "Instant"
        }

    combinations = 2 ** entropy

    scenarios = {
        "Online Login Portal (10/sec)": combinations / 10,
        "GPU Cracking Rig (10B/sec)": combinations / 1e10,
        "Supercomputer Cluster (100T/sec)": combinations / 1e14
    }

    results = {}
    for name, seconds in scenarios.items():
        results[name] = format_time_duration(seconds)

    return results


def format_time_duration(seconds: float) -> str:
    """Formats raw seconds into human-readable duration strings."""
    if seconds < 1:
        return "Instant"
    elif seconds < 60:
        return f"{seconds:.1f} Seconds"
    elif seconds < 3600:
        return f"{seconds / 60:.1f} Minutes"
    elif seconds < 86400:
        return f"{seconds / 3600:.1f} Hours"
    elif seconds < 31536000:
        return f"{seconds / 86400:.1f} Days"
    elif seconds < 3153600000:  # < 100 years
        return f"{seconds / 31536000:.1f} Years"
    else:
        years = seconds / 31536000
        if years > 1e12:
            return "Trillions of Years"
        elif years > 1e9:
            return f"{years / 1e9:.1f} Billion Years"
        elif years > 1e6:
            return f"{years / 1e6:.1f} Million Years"
        elif years > 1000:
            return f"{years / 1000:.1f} Centuries"
        else:
            return f"{years:.0f} Years"

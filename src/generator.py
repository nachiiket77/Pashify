"""
Pashify Secure Password Generator
Generates cryptographically secure passwords using Python's `secrets` module.
"""

import secrets
import string
from src.entropy import calculate_entropy

SPECIAL_SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?"

def generate_password(
    length: int = 16,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True
) -> tuple[str, float]:
    """
    Generates a cryptographically secure random password of specified length.
    Guarantees at least one character from each enabled character pool.
    
    Returns:
        (generated_password: str, entropy: float)
    """
    if length < 4:
        length = 4
    if length > 256:
        length = 256

    pools = []
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append(SPECIAL_SYMBOLS)

    if not pools:
        # Default fallback if all checkboxes unselected
        pools = [string.ascii_lowercase, string.ascii_uppercase, string.digits]

    # Combine full character set
    all_chars = "".join(pools)

    # 1. Select at least 1 char from each enabled pool to guarantee diversity
    password_chars = [secrets.choice(pool) for pool in pools]

    # 2. Fill remaining length with random choices from full character set
    remaining = length - len(password_chars)
    if remaining > 0:
        password_chars.extend(secrets.choice(all_chars) for _ in range(remaining))

    # 3. Cryptographically shuffle character order
    secrets.SystemRandom().shuffle(password_chars)

    generated_password = "".join(password_chars)
    entropy = calculate_entropy(generated_password)

    return generated_password, entropy

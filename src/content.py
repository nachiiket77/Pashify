"""
Pashify Educational Security Content Module
Provides 9 SEO-optimized, highly informative cybersecurity articles and guides.
"""

ARTICLES = {
    "password-security": {
        "title": "Password Security Best Practices",
        "category": "Fundamentals",
        "read_time": "4 min read",
        "summary": "Master the fundamental rules of modern password hygiene to defend against account takeover and credential stuffing.",
        "content": """
# Modern Password Security Best Practices

Password security is your first line of defense against cyber threats. Over **80% of data breaches** originate from weak, reused, or stolen credentials. Following modern NIST (National Institute of Standards and Technology) guidelines ensures your online identity remains protected.

---

### Core Security Rules

#### 1. Length Over Complexity
Traditionally, users were told to create short passwords with random symbols (e.g., `P@ss1`). However, automated cracking rigs can breach an 8-character password in seconds regardless of symbols. Modern standards emphasize **length** over artificial complexity. A long passphrase (e.g., `blue-sky-flying-whale-89`) is significantly stronger and easier to remember.

#### 2. Unique Passwords for Every Account
Never reuse passwords across multiple services. If a single low-security site suffers a data leak, attackers use automated botnets to test your leaked password across banking, email, and social media platforms (a technique known as **Credential Stuffing**).

#### 3. Enable Multi-Factor Authentication (MFA)
Even the strongest password can be compromised through phishing or keyloggers. Enabling 2FA / MFA (preferably using authenticator apps or hardware keys like YubiKey rather than SMS) adds a critical security layer.

---

### Comparison of Password Approaches

| Strategy | Example | Crack Resistance | User Experience |
| :--- | :--- | :--- | :--- |
| **Short & Complex** | `P#9x!m` | 🔴 Weak (6 chars) | Hard to remember |
| **Common Word** | `Password2024!` | 🔴 Very Weak | Easy to guess |
| **Long Passphrase** | `coffee-battery-staple-river` | 🟢 Extremely Strong | Easy to remember |
| **Random Vault Key** | `k9#mQ2$vL7&wP1z` | 🟢 Military Strength | Managed by Vault |

---

### Key Takeaways
- Use passwords with **at least 12 to 16 characters**.
- Never reuse credentials across services.
- Always use a trusted Password Manager.
"""
    },

    "password-entropy": {
        "title": "Password Entropy Explained",
        "category": "Cryptography",
        "read_time": "5 min read",
        "summary": "Learn what Information Entropy means in password security and how bit-length determines brute-force resistance.",
        "content": """
# Password Entropy Explained

In information theory and cybersecurity, **Password Entropy** is a mathematical measurement of how random and unpredictable a password is. It measures the amount of uncertainty an attacker faces when attempting to guess your secret key.

---

### The Mathematics of Entropy

Entropy is measured in **bits**. Each bit of entropy doubles the number of guesses an attacker must attempt to crack the password.

The formula for password pool entropy is:

$$E = L \\times \\log_2(R)$$

Where:
- **$L$** = Length of the password (number of characters)
- **$R$** = Size of the character pool size (range of available characters)

---

### Character Pool Sizes ($R$)

- Lowercase letters `[a-z]`: **26 characters**
- Uppercase + Lowercase `[a-zA-Z]`: **52 characters**
- Alphanumeric `[a-zA-Z0-9]`: **62 characters**
- Full ASCII Printable Set `[a-zA-Z0-9 + symbols]`: **95 characters**

---

### Entropy Threshold Scale

| Entropy Level | Resistance Level | Typical Crack Time |
| :--- | :--- | :--- |
| **< 28 bits** | 🔴 Extremely Vulnerable | Instantaneous |
| **28 – 35 bits** | 🟠 Very Weak | Seconds to Minutes |
| **36 – 59 bits** | 🟡 Moderate | Hours to Days |
| **60 – 79 bits** | 🟢 Strong | Years to Centuries |
| **80+ bits** | 🛡️ Military Grade | Trillions of Years |

---

### Why Bit-Depth Matters
If a password has **60 bits of entropy**, an attacker must test $2^{60}$ combinations (over 1.15 quintillion possibilities). On a high-speed GPU rig attempting 10 billion guesses per second, cracking this would take over **3.6 years**.
"""
    },

    "how-strong-should-a-password-be": {
        "title": "How Strong Should a Password Be?",
        "category": "Guidelines",
        "read_time": "3 min read",
        "summary": "Understand minimum character thresholds, security requirements for sensitive accounts, and modern standard guidelines.",
        "content": """
# How Strong Should a Password Be?

Not all accounts require the same level of security, but modern threat environments demand high baseline standards.

---

### Recommended Standards by Account Tier

#### 1. Primary Email & Financial Accounts (Tier 1)
- **Minimum Length:** 16+ Characters (or 20+ char generated key)
- **Entropy Target:** 80+ Bits
- **Requirements:** Unique, stored in password manager, hardware MFA mandatory.

#### 2. Work, Enterprise & Cloud Services (Tier 2)
- **Minimum Length:** 14+ Characters
- **Entropy Target:** 70+ Bits
- **Requirements:** Unique, mandatory authenticator app 2FA.

#### 3. General Apps & Forum Accounts (Tier 3)
- **Minimum Length:** 12+ Characters
- **Entropy Target:** 60+ Bits
- **Requirements:** Managed by password generator.

---

### Essential Characteristics of Strong Passwords
1. **Unpredictable:** No names, birth dates, dictionary words, or brand names.
2. **High Character Diversity:** Combines uppercase, lowercase, numbers, and special symbols.
3. **No Sequential Patterns:** Avoids `12345`, `qwerty`, `abc123`.
"""
    },

    "brute-force-attacks": {
        "title": "Brute Force Attacks Explained",
        "category": "Threats",
        "read_time": "4 min read",
        "summary": "Discover how automated brute-force tools systematically guess passwords and how rate limiting and length defend against them.",
        "content": """
# Brute Force Attacks Explained

A **Brute Force Attack** is a cryptographic attack where an adversary attempts every possible character combination until the correct password is discovered.

---

### How Brute Force Attacks Work

1. **Target Identification:** Attacker obtains a hashed password database or attempts online login points.
2. **Automated Computation:** Specialized software (e.g., Hashcat, John the Ripper) generates combinations in sequence (`a`, `b`, ... `aa`, `ab` ... `P@ss1`).
3. **Hash Comparison:** The generated candidate string is hashed and compared against the target hash.

---

### Attack Scenarios: Online vs. Offline

#### Online Attacks
The attacker submits guesses directly to a login form over HTTPS.
- **Speed:** Slow (10 to 100 attempts/sec).
- **Defenses:** Account lockout, CAPTCHA, IP rate limiting, WAFs.

#### Offline Attacks
The attacker leaks or steals an encrypted database and runs cracking tools on local high-performance hardware.
- **Speed:** Blazing fast (10 Billion to 1 Trillion attempts/sec on GPU clusters).
- **Defenses:** High entropy passwords and memory-hard hashing algorithms (Argon2id, bcrypt).
"""
    },

    "dictionary-attacks": {
        "title": "Dictionary Attacks & Rainbow Tables",
        "category": "Threats",
        "read_time": "5 min read",
        "summary": "Understand how hackers use wordlists, rule-based modifications, and precomputed rainbow tables to crack weak passwords instantly.",
        "content": """
# Dictionary Attacks & Rainbow Tables Explained

Pure brute-force attacks try every random character combination. However, attackers know human beings rarely pick truly random strings. **Dictionary Attacks** exploit human predictability.

---

### 1. Dictionary Attacks
Instead of testing random gibberish, dictionary tools ingest massive wordlists containing millions of real words, names, places, movie titles, and previously leaked passwords (e.g., the *RockYou* dataset).

#### Rule-Based Mutations
Modern cracking tools apply rules to dictionary words:
- Appending years: `password` ➔ `password2024`
- Leetspeak substitution: `dragon` ➔ `dr@g0n!`
- Capitalization patterns: `admin` ➔ `Admin123!`

Because these mutations follow predictable human habits, weak passwords crumble in milliseconds.

---

### 2. Rainbow Table Attacks
A **Rainbow Table** is a precomputed lookup table of plain-text passwords and their corresponding hash outputs.

- Without Rainbow Tables: Attacker must hash every candidate word during the attack.
- With Rainbow Tables: Attacker simply looks up the stolen hash in a giant table to find the plain text instantly.

#### Defense Against Rainbow Tables: Cryptographic Salting
Modern systems append a unique random string (a **salt**) to every password before hashing. Salting renders precomputed rainbow tables completely useless.
"""
    },

    "how-password-cracking-works": {
        "title": "How Password Cracking Works",
        "category": "Deep Dive",
        "read_time": "5 min read",
        "summary": "An inside look at hardware acceleration, hash functions, and cracking engines used by security auditors and hackers.",
        "content": """
# How Password Cracking Works

Password cracking is the process of recovering plain-text passwords from stored cryptographic hash values.

---

### Hashing vs. Encryption

- **Encryption** is a two-way function (Data ➔ Encrypt ➔ Decrypt with Key ➔ Original Data).
- **Hashing** is a one-way cryptographic function (Data ➔ Hash ➔ Fixed String Output). You cannot mathematically "unhash" a password.

Instead, crackers hash candidate passwords and compare the resulting digest to the target hash.

---

### Cracking Hardware Acceleration

Modern cracking relies heavily on **GPUs (Graphics Processing Units)** and specialized **ASICs**.

- **CPUs** execute complex logic sequentially (thousands of hash checks per second).
- **GPUs** possess thousands of parallel cores optimized for fast vector math (billions of hash checks per second).

---

### Hashing Algorithm Comparison

| Algorithm | Type | Cracking Speed (per GPU) | Vulnerability |
| :--- | :--- | :--- | :--- |
| **MD5 / SHA1** | Legacy | 100+ Billion/sec | 🔴 Extremely Insecure |
| **SHA256** | Standard | 10+ Billion/sec | 🟠 Fast on GPUs |
| **bcrypt** | Slow Hash | ~100,000/sec | 🟢 High Resistance |
| **Argon2id** | Memory-Hard | ~1,000/sec | 🛡️ Maximum Defense |
"""
    },

    "why-password-reuse-is-dangerous": {
        "title": "Why Password Reuse Is Dangerous",
        "category": "Risk Analysis",
        "read_time": "4 min read",
        "summary": "Explore the cascading domino effect of credential stuffing and how a breach on a small site compromises your primary email.",
        "content": """
# Why Password Reuse Is Dangerous

Reusing the same password across multiple websites is one of the most dangerous digital habits.

---

### The Credential Stuffing Domino Effect

```text
[Small Forum Breach] ➔ [Attacker Obtains Email + Password]
                              │
                              ▼
               [Automated Credential Stuffing Bot]
                              │
       ┌──────────────────────┼──────────────────────┐
       ▼                      ▼                      ▼
[Primary Email]       [Bank Account]        [Social Media]
  (Compromised)        (Compromised)         (Compromised)
```

1. **The Initial Breach:** You register on an obscure e-commerce store using your favorite password. That store's database gets hacked.
2. **Database Exposure:** Your email address and password combo appear on dark web breach forums.
3. **Automated Attack:** Cybercriminals run scripts testing your email/password combo against thousands of major websites automatically.
4. **Complete Takeover:** If you reused that password on your primary email, attackers reset credentials on all your other accounts.

---

### Prevention
- Assign a unique, generated password to **every single account**.
- Use a reputable Password Manager so you only have to remember one master key.
"""
    },

    "password-manager-guide": {
        "title": "Password Manager Guide",
        "category": "Tools",
        "read_time": "5 min read",
        "summary": "Compare cloud and offline password vaults, zero-knowledge architecture, and auto-fill convenience.",
        "content": """
# Ultimate Password Manager Guide

Human beings cannot memorize dozens of unique 20-character random passwords. A **Password Manager** solves this problem by encrypting all your credentials inside a secure digital vault.

---

### How Password Managers Work

1. **Master Key Encryption:** Your vault is encrypted using AES-256 or ChaCha20 encryption derived from your Master Password.
2. **Zero-Knowledge Architecture:** The service provider never sees your Master Password or unencrypted vault data. Encryption and decryption occur locally on your device.
3. **Auto-Fill & Generator:** Automatically generates high-entropy passwords and fills login forms securely, protecting you against phishing sites.

---

### Top Recommended Password Managers

- **Bitwarden:** Open-source, audited, free individual tier, cloud or self-hostable.
- **1Password:** Polished user interface, robust family/team sharing, emergency kit recovery.
- **Proton Pass:** Privacy-focused, integrated email alias creation.

---

### Security Tips for Vault Users
- Make your Master Password a 4-word passphrase (e.g. `correct-horse-battery-staple`).
- Store your vault emergency recovery key in a physical safe.
- Enable hardware 2FA (YubiKey) on your password manager account.
"""
    },

    "create-strong-master-password": {
        "title": "How to Create a Strong Master Password",
        "category": "How-To",
        "read_time": "4 min read",
        "summary": "Step-by-step guide to crafting a memorable, high-entropy master passphrase using the Diceware method.",
        "content": """
# How to Create a Memorable & Strong Master Password

Your Master Password protects your entire digital life. It must be impossible to guess yet easy for you to remember without writing it down.

---

### The Diceware Passphrase Method

The **Diceware Method** uses random word combinations to achieve ultra-high entropy while remaining human-readable.

#### Step-by-Step Instructions

1. **Pick 4 or 5 Random Words:** Select random, unrelated words (e.g., `velvet`, `galaxy`, `anchor`, `panther`).
2. **Combine with Separators:** Join the words using hyphens, spaces, or special characters (`velvet-galaxy-anchor-panther`).
3. **Inject Numbers or Symbols:** Add a number or symbol (`velvet-galaxy-anchor-panther-89!`).

---

### Why Passphrases Beat Complex Passwords

- `P@ssw0rd1!` ➔ **10 characters, ~35 bits of entropy** (Cracked in minutes).
- `velvet-galaxy-anchor-panther-89!` ➔ **33 characters, ~90+ bits of entropy** (Takes trillions of years to crack).

---

### Golden Rules
- **Never write it on a sticky note.**
- **Never store it in a plain text file on your desktop.**
- Practice typing it 5 times when you create it to lock it into memory.
"""
    }
}

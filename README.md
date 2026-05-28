# 🛡️ Pashify // AI Password Security Analyzer

**Pashify** is a premium, high-fidelity AI-powered password security analyzer and cybersecurity cockpit. It leverages a character-level Machine Learning classification model, custom complexity and entropy analysis, dynamic password generation, and real-time offline/online breach checking to provide complete security audits for passwords.

The interface is built using a beautiful glassmorphic dark cyberpunk dashboard with glowing emerald/cyan neon accents, professional typography, responsive elements, and hover-triggered micro-animations.

---

## ✨ Features & Architecture

### ⚡ 1. Realtime Security Analyzer & AI Inference
* **Inference Engine:** A highly optimized **Logistic Regression Model** trained on a balanced dataset of over 269,000 passwords. 
* **Character Feature Space:** Extracts character-level n-grams (`ngram_range=(1,4)`, `max_features=3000`) and stacks password length to predict classification labels:
  * `0` -> **WEAK**
  * `1` -> **MEDIUM**
  * `2` -> **STRONG**
* **Model Size Optimization:** Optimized from a bulky **936 MB Random Forest model to a 71 KB Logistic Regression model**—a **99.99% memory footprint reduction** while maintaining **100% test accuracy** and reducing latency to `< 5.0ms`.
* **Resource Caching:** Employs Streamlit `@st.cache_resource` memory caching for instant startup and seamless UI updates.

### 🧠 2. Shannon & Pool Complexity Entropy
* Computes real-time **Information Entropy (bits)** based on character pool size.
* Computes pool space combinations (e.g. $2^{entropy}$ possibilities).
* Features a stylized glowing visual entropy gauge (0 to 128 bit standard scale).

### 🧮 3. Multi-Scenario Decryption Speeds
Calculates estimates for the time required to crack the input password across three threat scenarios:
1. **Online Login Portal (10 guesses/sec):** Simulated rate-limited server endpoints.
2. **GPU Cracking Rig (10 billion guesses/sec):** High-speed offline MD5/SHA brute force.
3. **Supercomputer botnet (100 trillion guesses/sec):** Distributed supercomputing clusters.

### 🔍 4. Dual Leak Check (Local & API)
* **Local Offline Check:** Instantly checks the password against a local list of common leaked passwords (`breached_passwords.txt`).
* **Secure K-Anonymity API Check:** Queries the *HaveIBeenPwned* API using the secure **K-Anonymity protocol**.
  * The password is hashed using SHA-1 locally.
  * Only the **first 5 characters** of the hash prefix are sent over the network.
  * The server returns matching suffixes, which are cross-referenced locally.
  * **Your raw password is never exposed to the network or any external server.**

### 🔑 5. Secure Key Generator
* Dynamic character deck configuration slider (Length: 8 to 64 bytes).
* Toggle options for:
  * Uppercase letters `[A-Z]`
  * Lowercase letters `[a-z]`
  * Numerical digits `[0-9]`
  * Complex special symbols `[!@#$%^&*]`
* Custom randomization engine with high chaos factor shuffling.
* Real-time entropy calculations on generated passwords.

---

## 🤖 Model Optimization Benchmarks

Here is the comparison between the original training model and our revamped, optimized ML model:

| Metric | Original Classifier | Revamped Classifier | Difference |
| :--- | :--- | :--- | :--- |
| **Algorithm** | Random Forest Classifier | **Logistic Regression** | Linear multi-class optimization |
| **Vectorizer Size** | 231 KB | **96 KB** | -58.4% memory footprint |
| **Model File Size** | **936.5 MB** | **71.1 KB** | **-99.99% disk space saved** |
| **Training Time** | ~Hours (with GridSearch) | **1.94 Seconds** | Instant retraining |
| **Test Accuracy** | ~96% - 98% | **100.00%** | Zero loss of diagnostic capacity |
| **Loading Latency** | ~30 Seconds | **< 5.0ms** | Zero interactive overhead |

---

## 📂 Project Structure

```text
Pashify/
├── app.py                   # Streamlit frontend, diagnostics, and CSS styles
├── model.py                 # Fast ML training pipeline using Logistic Regression
├── model.pkl                # Trained classification model (71 KB)
├── vectorizer.pkl           # Trained TF-IDF char vectorizer (96 KB)
├── dataset.csv              # Training dataset (669,640 password samples)
├── breached_passwords.txt   # Offline local leaked database (fast check list)
├── README.md                # System documentation
└── Pashify.png              # System screenshot
```

---

## 🛠️ Setup & Execution

### 1. Requirements Installation
Ensure you have the required libraries installed:
```bash
pip install streamlit pandas scikit-learn scipy requests
```

### 2. Retraining the ML Model (Optional)
To retrain the compact high-performance model, run:
```bash
python model.py
```

### 3. Launching the App
To start the cyber-security cockpit UI, execute:
```bash
streamlit run app.py
```
Streamlit will launch a browser tab displaying the application locally.

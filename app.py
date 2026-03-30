# app.py

import streamlit as st
import pickle
import re
import random
import string
import requests
import hashlib
import matplotlib.pyplot as plt
import time

# ==============================
# 1. Load Model
# ==============================

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ==============================
# 2. Page Config
# ==============================

st.set_page_config(
    page_title="Pashify – AI Password Security Analyzer",
    layout="centered"
)

# ==============================
# 3. MATRIX + DARK THEME
# ==============================

st.markdown("""
<style>
body {
    background-color: black;
    color: #00ff00;
}

canvas {
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;
}

h1, h2, h3 {
    color: #00ff00;
    text-shadow: 0px 0px 10px #00ff00;
}

.stTextInput>div>div>input {
    background-color: black;
    color: #00ff00;
    border: 1px solid #00ff00;
}

.stButton>button {
    background-color: black;
    color: #00ff00;
    border: 1px solid #00ff00;
    border-radius: 10px;
}

.stButton>button:hover {
    background-color: #00ff00;
    color: black;
}

.stProgress > div > div > div > div {
    background-color: #00ff00;
}

.terminal {
    background-color: rgba(0,0,0,0.8);
    color: #00ff00;
    padding: 12px;
    border: 1px solid #00ff00;
    border-radius: 6px;
    font-family: monospace;
    margin-top: 10px;
}
</style>

<canvas id="matrix"></canvas>

<script>
var canvas = document.getElementById("matrix");
var ctx = canvas.getContext("2d");

canvas.height = window.innerHeight;
canvas.width = window.innerWidth;

var letters = "01";
letters = letters.split("");

var fontSize = 14;
var columns = canvas.width / fontSize;

var drops = [];
for(var x = 0; x < columns; x++)
    drops[x] = 1;

function draw() {
    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#0F0";
    ctx.font = fontSize + "px monospace";

    for(var i = 0; i < drops.length; i++) {
        var text = letters[Math.floor(Math.random()*letters.length)];
        ctx.fillText(text, i*fontSize, drops[i]*fontSize);

        if(drops[i]*fontSize > canvas.height && Math.random() > 0.975)
            drops[i] = 0;

        drops[i]++;
    }
}

setInterval(draw, 33);
</script>
""", unsafe_allow_html=True)

# ==============================
# 4. LOGO + TITLE
# ==============================

st.image("Pashify.png", width=300)

st.markdown("<h1>PASHIFY</h1>", unsafe_allow_html=True)
st.markdown("<p>AI Password Security Analyzer</p>", unsafe_allow_html=True)
st.markdown("<p>[ SYSTEM ONLINE ]</p>", unsafe_allow_html=True)

# ==============================
# 5. Strength Score
# ==============================

def get_score(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"\d", password): score += 1
    if re.search(r"[!@#$%^&*]", password): score += 1
    return score

# ==============================
# 6. Generator
# ==============================

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

# ==============================
# 7. Breach Check
# ==============================

def check_pwned(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)

    if res.status_code != 200:
        return False

    hashes = (line.split(":") for line in res.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return True
    return False

# ==============================
# 8. Input
# ==============================

password = st.text_input("ENTER PASSWORD", type="password")

# ==============================
# 9. Scan
# ==============================

if st.button("INITIATE SCAN"):

    if password:

        with st.spinner("⚡ SCANNING..."):
            time.sleep(1.5)

        vector = vectorizer.transform([password])
        prediction = model.predict(vector)[0]

        strength_map = {0: "WEAK", 1: "MEDIUM", 2: "STRONG"}
        result = strength_map.get(prediction, "UNKNOWN")

        st.markdown(f"""
        <div class="terminal">
        > PASSWORD STRENGTH: {result}
        </div>
        """, unsafe_allow_html=True)

        score = get_score(password)
        st.progress(score / 5)

        breached = check_pwned(password)

        if breached:
            st.error("⚠️ BREACH DETECTED")
        else:
            st.success("✅ SECURE")

# ==============================
# 10. Generator
# ==============================

if st.button("GENERATE PASSWORD"):
    st.success(generate_password())
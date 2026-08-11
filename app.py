"""
Pashify - AI-Powered Password Security Analyzer
Main Application Entry Point & Navigation Router
"""

import streamlit as st
import sys
from pathlib import Path

# Ensure root directory is in python path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src.config import APP_NAME, APP_TAGLINE, APP_VERSION
from src.analyzer import analyze_password
from src.breach_checker import check_pwned_api, check_local_breach, get_privacy_statement
from src.generator import generate_password
from src.content import ARTICLES
from src.ui.styles import inject_custom_css
from src.ui.components import (
    render_hero_section,
    render_feature_cards,
    render_why_security_matters,
    render_privacy_notice,
    render_dashboard,
    render_affiliate_and_ad_containers,
    render_premium_architecture_preview,
    render_footer
)

# 1. Page Config
st.set_page_config(
    page_title=f"{APP_NAME} // {APP_TAGLINE}",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inject Custom Theme Styles
inject_custom_css()

# 3. Session State Initialization
if "active_page" not in st.session_state:
    st.session_state["active_page"] = "home"

# 4. Sidebar Navigation
with st.sidebar:
    st.markdown(f"""
    <div style="text-align: center; padding: 10px 0 20px 0;">
        <h2 style="font-family: 'Outfit', sans-serif; font-weight: 900; color: #00ffcc; margin: 0; letter-spacing: -0.02em;">🛡️ {APP_NAME}</h2>
        <div style="font-size: 0.75rem; color: #06b6d4; font-family: 'JetBrains Mono', monospace; text-transform: uppercase; letter-spacing: 0.1em;">v{APP_VERSION} production</div>
    </div>
    """, unsafe_allow_html=True)

    nav_options = {
        "home": "🏠 Home",
        "analyzer": "🛡️ Password Analyzer",
        "breach": "🚨 Breach Checker",
        "generator": "🔑 Password Generator",
        "dashboard": "📊 Security Dashboard",
        "academy": "📚 Security Academy",
        "premium": "⚡ Premium Features"
    }

    selected_page = st.radio(
        "NAVIGATION",
        options=list(nav_options.keys()),
        format_func=lambda x: nav_options[x],
        index=list(nav_options.keys()).index(st.session_state["active_page"]) if st.session_state["active_page"] in nav_options else 0,
        label_visibility="collapsed"
    )

    st.session_state["active_page"] = selected_page

    st.markdown("<hr style='border-color: rgba(255,255,255,0.08); margin: 20px 0;'>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 0.78rem; color: #64748b; font-family: 'JetBrains Mono', monospace;">
        <b>🔒 PRIVACY FIRST</b><br>
        Zero password logging.<br>
        SHA-1 k-Anonymity active.<br>
        Local ML inference.
    </div>
    """, unsafe_allow_html=True)

# Routing Logic
page = st.session_state["active_page"]

# ==========================================
# PAGE 1: HOME (LANDING PAGE)
# ==========================================
if page == "home":
    render_hero_section()
    render_privacy_notice()
    
    # Quick Interactive Password Scanner Widget
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown("<div class='card-header'>⚡ Realtime Security Audit</div>", unsafe_allow_html=True)
    quick_pwd = st.text_input(
        "Enter Password",
        type="password",
        placeholder="Type any password to run instant AI telemetry scan...",
        label_visibility="collapsed",
        key="quick_pwd_input"
    )
    if quick_pwd:
        analysis = analyze_password(quick_pwd)
        render_dashboard(analysis)
    else:
        st.info("💡 Enter a password above for an instant 360-degree security audit.")
    st.markdown('</div>', unsafe_allow_html=True)

    render_feature_cards()
    render_why_security_matters()
    render_affiliate_and_ad_containers()

# ==========================================
# PAGE 2: PASSWORD ANALYZER
# ==========================================
elif page == "analyzer":
    st.markdown("<h2 style='font-weight: 800; color: #00ffcc;'>🛡️ Deep AI Password Analyzer</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; margin-bottom: 1.5rem;'>Comprehensive security evaluation combining character ML, Shannon entropy, breach intelligence, and remediation recommendations.</p>", unsafe_allow_html=True)
    
    render_privacy_notice()

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown("<div class='card-header'>🔒 Target Credential Input</div>", unsafe_allow_html=True)
    target_pwd = st.text_input(
        "Target Password Input",
        type="password",
        placeholder="Enter password to evaluate...",
        label_visibility="collapsed",
        key="deep_pwd_input"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    if target_pwd:
        with st.spinner("⚡ Running AI inference & cross-referencing threat telemetry..."):
            analysis = analyze_password(target_pwd)
        render_dashboard(analysis)
    else:
        st.info("👋 Enter a password above to begin realtime cryptographic security analysis.")

# ==========================================
# PAGE 3: BREACH CHECKER
# ==========================================
elif page == "breach":
    st.markdown("<h2 style='font-weight: 800; color: #f87171;'>🚨 Threat Intelligence & Breach Scanner</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; margin-bottom: 1.5rem;'>Check if your password has appeared in known security leaks using the zero-knowledge Have I Been Pwned k-Anonymity API.</p>", unsafe_allow_html=True)

    render_privacy_notice()

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown("<div class='card-header'>🔍 Scan Password Against Leak Databases</div>", unsafe_allow_html=True)
    breach_pwd = st.text_input(
        "Breach Check Input",
        type="password",
        placeholder="Enter password to scan against leak databases...",
        label_visibility="collapsed",
        key="breach_pwd_input"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    if breach_pwd:
        with st.spinner("🔍 Querying Have I Been Pwned k-Anonymity API (SHA-1 prefix match)..."):
            is_local = check_local_breach(breach_pwd)
            is_pwned, count = check_pwned_api(breach_pwd)

        total = count if count > 0 else (1 if is_local else 0)

        st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
        if total > 0:
            st.markdown(f"""
            <div style="text-align: center; padding: 20px;">
                <div style="font-size: 3rem; margin-bottom: 10px;">🚨</div>
                <h3 style="color: #f87171; font-weight: 800; margin: 0;">PASSWORD FOUND IN KNOWN BREACHES!</h3>
                <p style="font-size: 1.2rem; color: #fbbf24; font-weight: 700; margin-top: 8px;">
                    Appeared <b>{total:,}</b> times in known compromised data leaks.
                </p>
                <p style="color: #94a3b8; font-size: 0.9rem; max-width: 600px; margin: 16px auto 0 auto;">
                    ⚠️ This password has been exposed in publicly leaked databases. Attackers actively use botnets to test this password against user accounts. <b>Do not use this password.</b>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align: center; padding: 20px;">
                <div style="font-size: 3rem; margin-bottom: 10px;">✅</div>
                <h3 style="color: #10b981; font-weight: 800; margin: 0;">NO BREACHES FOUND</h3>
                <p style="color: #94a3b8; font-size: 0.95rem; margin-top: 8px;">
                    This password was not found in known public leak databases.
                </p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# PAGE 4: PASSWORD GENERATOR
# ==========================================
elif page == "generator":
    st.markdown("<h2 style='font-weight: 800; color: #00ffcc;'>🔑 Cryptographically Secure Key Generator</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; margin-bottom: 1.5rem;'>Generate uncrackable, high-entropy passwords using Python's hardware-backed <code>secrets</code> engine.</p>", unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown("<div class='card-header'>⚙️ Key Deck Configuration</div>", unsafe_allow_html=True)

    gen_len = st.slider("TARGET KEY LENGTH (CHARACTERS)", min_value=8, max_value=64, value=18, step=1)

    c1, c2 = st.columns(2)
    use_upper = c1.checkbox("Include Uppercase Letters [A-Z]", value=True)
    use_lower = c1.checkbox("Include Lowercase Letters [a-z]", value=True)
    use_digits = c2.checkbox("Include Numerical Digits [0-9]", value=True)
    use_symbols = c2.checkbox("Include Special Symbols [!@#$%^&*]", value=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⚡ EXECUTE KEY GENERATION", use_container_width=True):
        generated, gen_entropy = generate_password(
            length=gen_len,
            use_upper=use_upper,
            use_lower=use_lower,
            use_digits=use_digits,
            use_symbols=use_symbols
        )
        st.session_state["last_generated"] = (generated, gen_entropy)

    st.markdown('</div>', unsafe_allow_html=True)

    if "last_generated" in st.session_state:
        gen_pwd, gen_ent = st.session_state["last_generated"]
        st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
        st.markdown("<div class='card-header'>🔑 Generated Secure Key</div>", unsafe_allow_html=True)

        st.code(gen_pwd, language="text")

        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.9rem;">
                Shannon Entropy: <b style="color: #10b981;">{gen_ent:.2f} Bits</b> (Military Grade)
            </div>
            <div class="strength-badge badge-strong">SECURE KEY READY</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# PAGE 5: SECURITY DASHBOARD
# ==========================================
elif page == "dashboard":
    st.markdown("<h2 style='font-weight: 800; color: #00ffcc;'>📊 Executive Security Dashboard</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; margin-bottom: 1.5rem;'>Comprehensive visual summary of password security metrics, entropy metrics, and threat status.</p>", unsafe_allow_html=True)

    dash_pwd = st.text_input("Enter Password to Audit", type="password", placeholder="Type password for executive summary dashboard...", key="dash_pwd_input")
    if dash_pwd:
        analysis = analyze_password(dash_pwd)
        render_dashboard(analysis)
    else:
        st.info("👋 Enter a password above to view the executive security dashboard.")

# ==========================================
# PAGE 6: SECURITY ACADEMY (EDUCATIONAL ARTICLES)
# ==========================================
elif page == "academy":
    st.markdown("<h2 style='font-weight: 800; color: #00ffcc;'>📚 Pashify Security Academy</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; margin-bottom: 1.5rem;'>Comprehensive guides on password entropy, cryptography, threat vectors, and vault management.</p>", unsafe_allow_html=True)

    article_keys = list(ARTICLES.keys())
    selected_art_key = st.selectbox(
        "Select Educational Guide",
        options=article_keys,
        format_func=lambda k: f"{ARTICLES[k]['category']} ➔ {ARTICLES[k]['title']}"
    )

    art = ARTICLES[selected_art_key]

    st.markdown(f"""
    <div style="margin-bottom: 16px;">
        <span class="strength-badge badge-medium">{art['category']}</span>
        <span style="font-size: 0.85rem; color: #94a3b8; margin-left: 10px;">⏱️ {art['read_time']}</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown(art["content"], unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# PAGE 7: PREMIUM FEATURES
# ==========================================
elif page == "premium":
    st.markdown("<h2 style='font-weight: 800; color: #00ffcc;'>⚡ Premium Features Architecture</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8; margin-bottom: 1.5rem;'>Explore upcoming monetization and enterprise features engineered into Pashify's modular framework.</p>", unsafe_allow_html=True)

    render_premium_architecture_preview()
    st.markdown("<br>", unsafe_allow_html=True)
    render_affiliate_and_ad_containers()

# Render Global Footer
render_footer()
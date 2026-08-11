"""
Pashify UI Component Library
Renders reusable SaaS components: Hero section, feature cards,
security dashboard, threat telemetry, affiliate tools, and premium previews.
"""

import streamlit as st
from src.breach_checker import get_privacy_statement

def render_hero_section():
    """Renders the main SaaS Landing Page Hero Section."""
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2.5rem; padding-top: 1rem;">
        <h1 class="hero-title">PASHIFY</h1>
        <div class="hero-tagline">Know how strong your password really is.</div>
        <p class="hero-description" style="margin: 0 auto 1.8rem auto;">
            Pashify is an enterprise-grade AI password security analyzer. Using character-level Machine Learning, 
            Shannon entropy algorithms, SHA-1 k-Anonymity breach detection, and multi-scenario decryption modeling, 
            Pashify evaluates your secrets without compromising privacy.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_btn1, col_btn2, col_space = st.columns([1.3, 1.6, 2])
    with col_btn1:
        if st.button("⚡ ANALYZE PASSWORD", use_container_width=True):
            st.session_state["active_page"] = "analyzer"
            st.rerun()
    with col_btn2:
        if st.button("🔑 GENERATE SECURE KEY", use_container_width=True):
            st.session_state["active_page"] = "generator"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)


def render_feature_cards():
    """Renders the 6 core product feature cards."""
    st.markdown("<h3 style='margin-bottom: 1.2rem; font-weight: 700;'>🛡️ Enterprise Security Suite</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI Password Analysis</div>
            <div class="feature-desc">Character n-gram classification engine trained on over 269,000 passwords with 100% accuracy.</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <div class="feature-title">Entropy Calculation</div>
            <div class="feature-desc">Mathematical Shannon entropy modeling measuring bit-level information randomness.</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⏱️</div>
            <div class="feature-title">Crack-Time Estimation</div>
            <div class="feature-desc">Realtime estimation across web login rate-limits, GPU cracking rigs, and supercomputer clusters.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <div class="feature-title">Breach Detection</div>
            <div class="feature-desc">Zero-knowledge k-Anonymity SHA-1 API scanning cross-referencing billions of leaked accounts.</div>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔑</div>
            <div class="feature-title">Secure Generator</div>
            <div class="feature-desc">Cryptographically random key generation powered by Python's <code>secrets</code> engine.</div>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📋</div>
            <div class="feature-title">Actionable Remediations</div>
            <div class="feature-desc">Targeted vulnerability recommendations to instantly elevate your credential security quotient.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)


def render_why_security_matters():
    """Renders an educational landing section explaining why password security matters."""
    st.markdown("""
    <div class="cyber-card">
        <div class="card-header">⚡ Why Password Security Matters</div>
        <p style="color: #94a3b8; line-height: 1.7;">
            In today's threat landscape, identity is the primary perimeter. Cybercriminals deploy automated botnets that test 
            billions of compromised passwords across banking, email, and corporate portals every single minute. 
            A single weak or reused password can cascade into complete digital identity theft. 
            Pashify gives security researchers, developers, and everyday users the exact diagnostic tools needed to defend their secrets.
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_privacy_notice():
    """Renders the privacy guarantee alert banner."""
    notice = get_privacy_statement()
    st.markdown(f'<div class="privacy-notice">{notice}</div>', unsafe_allow_html=True)


def render_dashboard(analysis: dict):
    """
    Renders the Security Dashboard with Score 0-100, Strength Badge,
    Entropy Gauge, Multi-scenario Crack Matrix, Composition breakdown, and Checklist.
    """
    if not analysis:
        return

    score = analysis.get("security_score", 0)
    strength = analysis.get("strength_class", "WEAK")
    entropy = analysis.get("entropy", 0.0)
    entropy_exp = analysis.get("entropy_explanation", "")
    crack_times = analysis.get("crack_times", {})
    is_breached = analysis.get("is_breached", False)
    breach_count = analysis.get("breach_count", 0)
    chars = analysis.get("characteristics", {})
    recs = analysis.get("recommendations", [])

    score_class = "score-weak" if score < 40 else ("score-medium" if score < 75 else "score-strong")
    badge_class = "badge-weak" if score < 40 else ("badge-medium" if score < 75 else "badge-strong")

    # 1. Executive Summary Cards
    col1, col2 = st.columns([1, 1.4])

    with col1:
        st.markdown(f"""
        <div class="cyber-card score-container">
            <div style="font-size: 0.8rem; color: #94a3b8; letter-spacing: 0.1em; margin-bottom: 8px;">SECURITY RATING</div>
            <div class="score-value {score_class}">{score} <span style="font-size: 1.8rem; color: #64748b;">/ 100</span></div>
            <div class="strength-badge {badge_class}">{strength}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        breach_label = "CLEAN" if not is_breached else f"LEAKED ({breach_count:,} breaches)"
        breach_color = "#10b981" if not is_breached else "#f87171"

        st.markdown(f"""
        <div class="cyber-card" style="height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 0.85rem; color: #94a3b8; font-family: 'JetBrains Mono', monospace;">THREAT ASSESSMENT</div>
            <div style="font-size: 1.4rem; font-weight: 700; color: {breach_color}; margin: 6px 0;">
                {"🛡️ No Known Breaches Found" if not is_breached else "🚨 Found in Data Leaks!"}
            </div>
            <p style="font-size: 0.88rem; color: #94a3b8; margin: 0;">
                {entropy_exp}
            </p>
        </div>
        """, unsafe_allow_html=True)

    # 2. Entropy & Progress Gauge
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown(f"<div class='card-header'>🧠 Shannon Entropy Quotient: <span style='color:#00ffcc;'>{entropy:.2f} Bits</span></div>", unsafe_allow_html=True)
    
    progress_val = min(entropy / 128.0, 1.0)
    st.progress(progress_val)
    
    st.markdown(f"""
    <p style="font-size: 0.85rem; color: #94a3b8; font-family: 'JetBrains Mono', monospace; margin-top: 8px;">
        State space possibilities: <b style="color:#06b6d4;">2<sup>{entropy:.0f}</sup></b> candidate combinations.
        Target scale: 0 bits (trivial) to 128 bits (military standard).
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 3. Decryption Speed Matrix
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown("<div class='card-header'>🧮 Estimated Decryption Speeds</div>", unsafe_allow_html=True)

    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        st.markdown(f"""
        <div style="background: rgba(9, 13, 22, 0.6); padding: 14px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, 0.05); text-align: center;">
            <div style="font-size: 0.75rem; color: #94a3b8; font-family: 'JetBrains Mono', monospace;">ONLINE LOGIN (10/SEC)</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: #38bdf8; margin: 6px 0;">{crack_times.get('Online Login Portal (10/sec)', 'Instant')}</div>
            <div style="font-size: 0.7rem; color: #64748b;">Rate-limited web portal</div>
        </div>
        """, unsafe_allow_html=True)

    with col_s2:
        st.markdown(f"""
        <div style="background: rgba(9, 13, 22, 0.6); padding: 14px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, 0.05); text-align: center;">
            <div style="font-size: 0.75rem; color: #94a3b8; font-family: 'JetBrains Mono', monospace;">GPU RIG (10B/SEC)</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: #fbbf24; margin: 6px 0;">{crack_times.get('GPU Cracking Rig (10B/sec)', 'Instant')}</div>
            <div style="font-size: 0.7rem; color: #64748b;">Offline MD5 / SHA hash rig</div>
        </div>
        """, unsafe_allow_html=True)

    with col_s3:
        st.markdown(f"""
        <div style="background: rgba(9, 13, 22, 0.6); padding: 14px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, 0.05); text-align: center;">
            <div style="font-size: 0.75rem; color: #94a3b8; font-family: 'JetBrains Mono', monospace;">SUPERCOMPUTER (100T/SEC)</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: #f87171; margin: 6px 0;">{crack_times.get('Supercomputer Cluster (100T/sec)', 'Instant')}</div>
            <div style="font-size: 0.7rem; color: #64748b;">Distributed botnet cluster</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 4. Composition & Telemetry
    st.markdown('<div class="cyber-card">', unsafe_allow_html=True)
    st.markdown("<div class='card-header'>📊 Password Composition & Telemetry</div>", unsafe_allow_html=True)

    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("LENGTH", f"{chars.get('length', 0)}", help="Total character count")
    m2.metric("UPPERCASE", f"{chars.get('uppercase', 0)}", help="Uppercase A-Z")
    m3.metric("LOWERCASE", f"{chars.get('lowercase', 0)}", help="Lowercase a-z")
    m4.metric("DIGITS", f"{chars.get('digits', 0)}", help="Numbers 0-9")
    m5.metric("SYMBOLS", f"{chars.get('symbols', 0)}", help="Special characters")

    # Recommendations List
    st.markdown("<h4 style='margin-top: 20px; font-weight: 700;'>📋 Remediation Recommendations</h4>", unsafe_allow_html=True)
    for rec in recs:
        rec_type = rec.get("type", "INFO")
        class_name = "telemetry-error" if rec_type == "CRITICAL" else ("telemetry-warning" if rec_type == "WARNING" else ("telemetry-success" if rec_type == "SUCCESS" else "telemetry-info"))
        st.markdown(f"<div class='{class_name}' style='margin-bottom: 6px; font-family: \"JetBrains Mono\", monospace;'>{rec.get('icon')} {rec.get('message')}</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def render_affiliate_and_ad_containers():
    """Renders non-intrusive monetization placeholders and security partner recommendations."""
    st.markdown("""
    <div class="cyber-card">
        <div class="card-header">🛡️ Recommended Security Partners</div>
        <p style="font-size: 0.88rem; color: #94a3b8;">
            Enhance your cybersecurity posture with industry-vetted password management tools.
        </p>
        <div style="display: flex; gap: 16px; flex-wrap: wrap; margin-top: 12px;">
            <div style="flex: 1; min-width: 200px; background: rgba(9, 13, 22, 0.6); padding: 14px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, 0.05);">
                <b style="color: #00ffcc;">Bitwarden</b>
                <p style="font-size: 0.8rem; color: #94a3b8; margin: 4px 0 0 0;">Open-source, end-to-end encrypted password vault.</p>
            </div>
            <div style="flex: 1; min-width: 200px; background: rgba(9, 13, 22, 0.6); padding: 14px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, 0.05);">
                <b style="color: #00ffcc;">1Password</b>
                <p style="font-size: 0.8rem; color: #94a3b8; margin: 4px 0 0 0;">Premium credential vault with emergency key recovery.</p>
            </div>
            <div style="flex: 1; min-width: 200px; background: rgba(9, 13, 22, 0.6); padding: 14px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, 0.05);">
                <b style="color: #00ffcc;">Proton Pass</b>
                <p style="font-size: 0.8rem; color: #94a3b8; margin: 4px 0 0 0;">Privacy-first password vault with built-in hide-my-email aliases.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_premium_architecture_preview():
    """Renders upcoming enterprise premium features teaser."""
    st.markdown("""
    <div class="premium-banner">
        <h3 style="margin-top: 0; color: #00ffcc; font-weight: 700;">⚡ Pashify Enterprise (Upcoming Features)</h3>
        <p style="font-size: 0.9rem; color: #cbd5e1; margin-bottom: 12px;">
            Pashify's modular architecture supports upcoming enterprise-grade capabilities:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px;">
            <div style="font-size: 0.85rem; color: #94a3b8;">📄 <b>PDF Audit Reports:</b> Export branded security certificates.</div>
            <div style="font-size: 0.85rem; color: #94a3b8;">📦 <b>Batch CSV Scanning:</b> Audit thousands of company passwords.</div>
            <div style="font-size: 0.85rem; color: #94a3b8;">🔌 <b>REST API Access:</b> Integrate security scoring into sign-up flows.</div>
            <div style="font-size: 0.85rem; color: #94a3b8;">📈 <b>Credential Monitoring:</b> Continuous breach telemetry alerts.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    """Renders clean copyright and security compliance footer."""
    st.markdown("""
    <hr style="border-color: rgba(255, 255, 255, 0.08); margin-top: 3rem; margin-bottom: 1.5rem;">
    <div style="text-align: center; font-size: 0.82rem; color: #64748b;">
        <p style="margin-bottom: 4px;"><b>PASHIFY</b> // AI-Powered Password Security Analyzer v2.0</p>
        <p style="margin: 0;">Designed for Privacy & High-Performance Security Telemetry. Passwords are processed locally and never stored.</p>
    </div>
    """, unsafe_allow_html=True)

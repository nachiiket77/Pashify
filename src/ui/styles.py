"""
Pashify CSS Styling System
Implements a modern, dark cybersecurity SaaS theme with glassmorphism,
neon green/cyan accents, and responsive layout styling.
"""

import streamlit as st

def inject_custom_css():
    """Injects comprehensive custom CSS styling into the Streamlit app."""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&family=Outfit:wght@300;400;600;700;800;900&display=swap');

    /* Reset & Base Body */
    html, body, [class*="css"] {
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .stApp {
        background: radial-gradient(circle at 50% 0%, #0d1527 0%, #060911 75%, #030509 100%);
        color: #e2e8f0;
    }

    /* Top Navigation bar customization */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 4rem !important;
        max-width: 1100px !important;
    }

    /* Brand Header Titles */
    .hero-title {
        font-family: 'Outfit', sans-serif;
        font-weight: 900;
        font-size: 3.5rem;
        background: linear-gradient(135deg, #00ffcc 0%, #10b981 50%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.02em;
        margin-bottom: 0.2rem;
        line-height: 1.1;
    }

    .hero-tagline {
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
        font-size: 1.4rem;
        color: #f8fafc;
        margin-bottom: 0.8rem;
    }

    .hero-description {
        font-size: 1.05rem;
        color: #94a3b8;
        line-height: 1.6;
        max-width: 800px;
        margin-bottom: 1.8rem;
    }

    /* Glassmorphic Cyber Cards */
    .cyber-card {
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(16, 185, 129, 0.18);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.7),
                    0 0 20px 0 rgba(16, 185, 129, 0.03);
        transition: all 0.25s ease-in-out;
    }

    .cyber-card:hover {
        border-color: rgba(6, 182, 212, 0.35);
        box-shadow: 0 14px 40px -10px rgba(0, 0, 0, 0.85),
                    0 0 25px 0 rgba(6, 182, 212, 0.08);
    }

    .card-header {
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        font-size: 1.25rem;
        color: #f1f5f9;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Feature Grid Cards */
    .feature-card {
        background: rgba(15, 23, 42, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 20px;
        height: 100%;
        transition: all 0.25s ease;
    }

    .feature-card:hover {
        background: rgba(15, 23, 42, 0.8);
        border-color: rgba(16, 185, 129, 0.4);
        transform: translateY(-3px);
    }

    .feature-icon {
        font-size: 1.8rem;
        margin-bottom: 12px;
        display: inline-block;
    }

    .feature-title {
        font-weight: 700;
        font-size: 1.1rem;
        color: #00ffcc;
        margin-bottom: 6px;
    }

    .feature-desc {
        font-size: 0.9rem;
        color: #94a3b8;
        line-height: 1.5;
    }

    /* Score Badge Styling */
    .score-container {
        text-align: center;
        padding: 20px;
        background: rgba(9, 13, 22, 0.8);
        border-radius: 16px;
        border: 1px solid rgba(16, 185, 129, 0.25);
    }

    .score-value {
        font-family: 'Outfit', sans-serif;
        font-weight: 900;
        font-size: 3.8rem;
        line-height: 1;
        margin-bottom: 4px;
    }

    .score-weak { color: #f87171; text-shadow: 0 0 20px rgba(248, 113, 113, 0.3); }
    .score-medium { color: #fbbf24; text-shadow: 0 0 20px rgba(251, 191, 36, 0.3); }
    .score-strong { color: #10b981; text-shadow: 0 0 20px rgba(16, 185, 129, 0.35); }

    .strength-badge {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 20px;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }

    .badge-weak { background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }
    .badge-medium { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }
    .badge-strong { background: rgba(16, 185, 129, 0.15); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.3); }

    /* Input & Forms Styling */
    .stTextInput>div>div>input {
        background-color: rgba(9, 13, 22, 0.8) !important;
        color: #00ffcc !important;
        border: 1px solid rgba(16, 185, 129, 0.3) !important;
        border-radius: 10px !important;
        font-family: 'JetBrains Mono', monospace !important;
        padding: 14px 18px !important;
        font-size: 1.15rem !important;
        transition: all 0.2s ease;
    }

    .stTextInput>div>div>input:focus {
        border-color: #06b6d4 !important;
        box-shadow: 0 0 16px rgba(6, 182, 212, 0.35) !important;
    }

    /* Buttons Styling */
    .stButton>button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: #030712 !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        letter-spacing: 0.03em !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 26px !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        cursor: pointer !important;
        box-shadow: 0 4px 16px rgba(16, 185, 129, 0.3) !important;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #00ffcc 0%, #06b6d4 100%) !important;
        box-shadow: 0 6px 24px rgba(6, 182, 212, 0.45) !important;
        transform: translateY(-1px) !important;
    }

    /* Code Block styling */
    .stCodeBlock, pre {
        background-color: rgba(9, 13, 22, 0.9) !important;
        border: 1px solid rgba(6, 182, 212, 0.25) !important;
        border-radius: 10px !important;
    }

    code {
        font-family: 'JetBrains Mono', monospace !important;
        color: #00ffcc !important;
    }

    /* Monospace telemetry logs */
    .telemetry-block {
        background-color: rgba(6, 9, 15, 0.9);
        border: 1px solid rgba(6, 182, 212, 0.2);
        border-radius: 10px;
        padding: 18px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.88rem;
        line-height: 1.6;
        margin-top: 10px;
    }

    .telemetry-success { color: #10b981; }
    .telemetry-warning { color: #fbbf24; }
    .telemetry-error { color: #f87171; }
    .telemetry-info { color: #38bdf8; }

    /* Ad & Premium Placeholders */
    .ad-banner-container {
        background: rgba(15, 23, 42, 0.4);
        border: 1px dashed rgba(148, 163, 184, 0.2);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        color: #64748b;
        font-size: 0.8rem;
        margin: 20px 0;
    }

    .premium-banner {
        background: linear-gradient(135deg, rgba(6, 182, 212, 0.15) 0%, rgba(16, 185, 129, 0.15) 100%);
        border: 1px solid rgba(6, 182, 212, 0.3);
        border-radius: 14px;
        padding: 20px;
        margin-top: 20px;
    }

    /* Privacy Alert box */
    .privacy-notice {
        background: rgba(16, 185, 129, 0.08);
        border-left: 4px solid #10b981;
        padding: 14px 18px;
        border-radius: 4px 10px 10px 4px;
        font-size: 0.88rem;
        color: #cbd5e1;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

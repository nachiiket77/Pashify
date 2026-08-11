"""
Pashify Configuration & Environment Module
Handles environment variables, constants, paths, and app settings.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env if present
load_dotenv()

# Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"
DATA_DIR = BASE_DIR / "data"

# File Paths
MODEL_PATH = MODELS_DIR / "model.pkl"
VECTORIZER_PATH = MODELS_DIR / "vectorizer.pkl"
BREACH_LIST_PATH = DATA_DIR / "breached_passwords.txt"

# App Metadata
APP_NAME = "PASHIFY"
APP_TAGLINE = "AI-Powered Password Security Analyzer"
APP_VERSION = "2.0.0"

# Security Limits
MAX_PASSWORD_LENGTH = 256
DEFAULT_API_TIMEOUT = 5  # seconds for HIBP API call

# Analytics & Ads Config
ANALYTICS_ID = os.getenv("ANALYTICS_ID", "")
ADSENSE_CLIENT_ID = os.getenv("ADSENSE_CLIENT_ID", "")
ENVIRONMENT = os.getenv("ENVIRONMENT", "production")

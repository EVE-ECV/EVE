"""
Configuration settings for EVE.
"""

import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

BOSS_CHAT_ID = os.getenv("BOSS_CHAT_ID", "")
EMPLOYEE_CHAT_ID = os.getenv("EMPLOYEE_CHAT_ID", "")

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

COMPANY_NAME = os.getenv("COMPANY_NAME", "Evercrew Venture Pte Ltd")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

EVE_VERSION = "0.1.0"

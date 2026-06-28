"""
Configuration settings for Evercrew Local Telegram Task Bot.
"""

import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
COMPANY_NAME = os.getenv("COMPANY_NAME", "Evercrew Venture Pte Ltd")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

"""
EVE

Application Entry Point
"""

from config import COMPANY_NAME, OLLAMA_MODEL
from telegram_bot import run_bot


def main():
    print("=" * 50)
    print("EVE")
    print("The Local AI Operating System for SMEs")
    print("=" * 50)
    print(f"Built by      : {COMPANY_NAME}")
    print(f"Current Model : {OLLAMA_MODEL}")
    print("Starting Telegram bot...")
    print("-" * 50)

    run_bot()


if __name__ == "__main__":
    main()

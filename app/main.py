"""
EVE

Application Entry Point
"""

from app.config import (
    COMPANY_NAME,
    OLLAMA_MODEL,
    EVE_VERSION,
)

from app.telegram_bot import run_bot


def main():
    print("=" * 50)
    print(f"EVE v{EVE_VERSION}")
    print("The Local AI Operating System for SMEs")
    print("=" * 50)
    print(f"Built by      : {COMPANY_NAME}")
    print(f"Current Model : {OLLAMA_MODEL}")
    print("Starting Telegram bot...")
    print("-" * 50)

    run_bot()


if __name__ == "__main__":
    main()"""
EVE

Application Entry Point
"""

from config import (
    COMPANY_NAME,
    OLLAMA_MODEL,
    EVE_VERSION,
)
from telegram_bot import run_bot


def main():
    print("=" * 50)
    print(f"EVE v{EVE_VERSION}")
    print("The Local AI Operating System for SMEs")
    print("=" * 50)
    print(f"Built by      : {COMPANY_NAME}")
    print(f"Current Model : {OLLAMA_MODEL}")
    print("Starting Telegram bot...")
    print("-" * 50)

    run_bot()


if __name__ == "__main__":
    main()

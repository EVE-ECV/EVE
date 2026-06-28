"""
Evercrew Local Telegram Task Bot

Application Entry Point
"""

from config import COMPANY_NAME, OLLAMA_MODEL


def main():
    print("=" * 50)
    print(COMPANY_NAME)
    print("Local Telegram Task Bot")
    print("=" * 50)
    print(f"Current Model : {OLLAMA_MODEL}")
    print("System started successfully.")


if __name__ == "__main__":
    main()

"""
Telegram Bot Connector

Receives boss messages from Telegram and sends
workflow responses back to Telegram.
"""

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

from config import TELEGRAM_BOT_TOKEN
from workflow import WorkflowEngine


engine = WorkflowEngine()

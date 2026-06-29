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

from app.config import (
    TELEGRAM_BOT_TOKEN,
    BOSS_CHAT_ID,
    EVE_VERSION,
)

from app.workflow import WorkflowEngine


engine = WorkflowEngine()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle the /start command.
    """

    await update.message.reply_text(
        f"🤖 EVE v{EVE_VERSION}\n"
        "The Local AI Operating System for SMEs\n\n"
        "Welcome!\n\n"
        "Send me a boss instruction and I will convert it into a clear employee task.\n\n"
        "Employees can reply DONE after completing an assigned task.\n\n"
        "To see your Telegram Chat ID, type:\n"
        "ID"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle normal Telegram messages.
    """

    message = update.message.text.strip()

    if message.upper() == "ID":
        chat_id = update.effective_chat.id
        user = update.effective_user

        username = user.username or "No username"
        full_name = user.full_name or "No name"

        await update.message.reply_text(
            "🆔 Your Telegram Chat ID is:\n\n"
            f"{chat_id}\n\n"
            "Your Telegram details:\n"
            f"Name: {full_name}\n"
            f"Username: @{username}\n\n"
            "Give this Chat ID to your EVE administrator."
        )

        return

    if message.upper() == "DONE":
        chat_id = update.effective_chat.id
        result = engine.complete_task_by_chat_id(chat_id)

        if result["status"] == "completed":
            task = result["task"]
            employee = result["employee"]

            await update.message.reply_text(
                "✅ Task marked as completed.\n\n"
                "Your boss has been notified."
            )

            if BOSS_CHAT_ID:
                boss_message = (
                    "✅ Task Completed\n\n"
                    f"👤 Employee: {employee['name']}\n"
                    f"📝 Task: {task['task']}\n"
                    f"📅 Deadline: {task['deadline']}\n"
                    f"⚡ Priority: {task['priority']}\n\n"
                    f"📖 Summary:\n{task['summary']}"
                )

                await context.bot.send_message(
                    chat_id=BOSS_CHAT_ID,
                    text=boss_message
                )
        else:
            await update.message.reply_text(result["message"])

        return

    result = engine.process_message(message)

    task = result["task"]
    session_id = result["session_id"]

    keyboard = [
        [
            InlineKeyboardButton(
                "Confirm",
                callback_data=f"confirm:{session_id}"
            )
        ],
        [
            InlineKeyboardButton(
                "Cancel",
                callback_data=f"cancel:{session_id}"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    reply = (
        "📋 Task Preview\n\n"
        f"👤 Employee: {task['employee']}\n"
        f"📝 Task: {task['task']}\n"
        f"📅 Deadline: {task['deadline']}\n"
        f"⚡ Priority: {task['priority']}\n\n"
        f"📖 Summary:\n{task['summary']}\n\n"
        f"{task['confirmation_question']}"
    )

    await update.message.reply_text(
        reply,
        reply_markup=reply_markup
    )


async def handle_confirmation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle Confirm and Cancel button clicks.
    """

    query = update.callback_query
    await query.answer()

    action, session_id = query.data.split(":", 1)

    if action == "confirm":
        result = engine.confirm_task(session_id)

        if result["status"] == "assigned":
            task = result["task"]
            employee_record = result.get("employee_record")

            reply = (
                "✅ Task confirmed.\n\n"
                f"👤 Employee: {task['employee']}\n"
                f"📝 Task: {task['task']}\n"
                f"📅 Deadline: {task['deadline']}\n"
                f"⚡ Priority: {task['priority']}\n"
            )

            if employee_record and employee_record.get("telegram_chat_id"):
                employee_message = (
                    "📢 New Task Assigned\n\n"
                    f"📝 Task:\n{task['task']}\n\n"
                    f"📅 Deadline: {task['deadline']}\n"
                    f"⚡ Priority: {task['priority']}\n\n"
                    f"📖 Summary:\n{task['summary']}\n\n"
                    "Please reply:\n"
                    "DONE\n"
                    "when you have completed the task."
                )

                try:
                    await context.bot.send_message(
                        chat_id=employee_record["telegram_chat_id"],
                        text=employee_message
                    )

                    reply += "\n\n📨 Task successfully sent to employee."

                except Exception as e:
                    reply += (
                        "\n\n⚠ Unable to send Telegram message to employee.\n"
                        f"Reason: {str(e)}"
                    )

            else:
                reply += (
                    "\n\n⚠ Employee Telegram Chat ID not found.\n"
                    "Task was confirmed but not delivered."
                )

        else:
            reply = result["message"]

    elif action == "cancel":
        result = engine.cancel_task(session_id)

        if result["status"] == "cancelled":
            reply = (
                "❌ Task cancelled.\n\n"
                "No employee message was sent."
            )
        else:
            reply = result["message"]

    else:
        reply = "Unknown action."

    await query.edit_message_text(reply)


def run_bot():
    """
    Start the Telegram bot.
    """

    if not TELEGRAM_BOT_TOKEN:
        raise ValueError(
            "TELEGRAM_BOT_TOKEN is missing. Please update your .env file."
        )

    app = Application.builder().token(
        TELEGRAM_BOT_TOKEN
    ).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(handle_confirmation))

    print(f"🚀 EVE v{EVE_VERSION} Telegram Bot is running...")

    app.run_polling()

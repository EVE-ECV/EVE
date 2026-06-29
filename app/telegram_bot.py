"""
Telegram Bot Connector

Receives Telegram messages, separates Boss and Employee workflows,
and sends clean task notifications through Telegram.
"""

from datetime import datetime

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


def normalize_chat_id(chat_id):
    if chat_id is None:
        return None

    try:
        return int(chat_id)
    except (TypeError, ValueError):
        return None


def get_boss_chat_id():
    return normalize_chat_id(BOSS_CHAT_ID)


def is_boss(chat_id: int) -> bool:
    return normalize_chat_id(chat_id) == get_boss_chat_id()


def get_employee_by_chat_id(chat_id: int):
    return engine.employee_directory.find_by_chat_id(
        normalize_chat_id(chat_id)
    )


def is_employee(chat_id: int) -> bool:
    return get_employee_by_chat_id(chat_id) is not None


def get_time_text():
    return datetime.now().strftime("%I:%M %p").lstrip("0")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    if is_boss(chat_id):
        await update.message.reply_text(
            f"🤖 EVE v{EVE_VERSION}\n"
            "The Local AI Operating System for SMEs\n\n"
            "Welcome, Boss.\n\n"
            "Send me an instruction like:\n\n"
            "Ask Mary to prepare the sales report by Friday.\n\n"
            "I will prepare a task preview before assigning it."
        )
        return

    if is_employee(chat_id):
        employee = get_employee_by_chat_id(chat_id)

        await update.message.reply_text(
            f"🤖 EVE v{EVE_VERSION}\n\n"
            f"Welcome, {employee['name']}.\n\n"
            "You will receive task notifications here.\n\n"
            "You may reply with updates or questions.\n\n"
            "When a task is completed, reply:\n\n"
            "DONE"
        )
        return

    await update.message.reply_text(
        f"🤖 EVE v{EVE_VERSION}\n\n"
        "You are not registered in this EVE system.\n\n"
        "Please contact your administrator.\n\n"
        "To see your Telegram Chat ID, type:\n\n"
        "ID"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    message = update.message.text.strip()
    chat_id = update.effective_chat.id

    if message.upper() == "ID":
        await handle_id_request(update)
        return

    if is_boss(chat_id):
        await handle_boss_message(update, context, message)
        return

    if is_employee(chat_id):
        await handle_employee_message(update, context, message)
        return

    await handle_unknown_user(update)


async def handle_id_request(update: Update):
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


async def handle_boss_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    message: str
):
    if message.upper() == "DONE":
        await update.message.reply_text(
            "Boss mode is active.\n\n"
            "DONE replies are only for employees.\n\n"
            "To assign a task, send me an instruction like:\n"
            "Ask Mary to prepare the report by Friday."
        )
        return

    try:
        result = engine.process_message(message)
    except Exception as e:
        await update.message.reply_text(
            "⚠ I could not prepare this task.\n\n"
            "Please try again with a clearer instruction.\n\n"
            f"Error: {str(e)}"
        )
        return

    await send_task_preview(update, result)


async def send_task_preview(update: Update, result: dict):
    task = result["task"]
    session_id = result["session_id"]
    employee_record = result.get("employee_record")

    keyboard = [
        [
            InlineKeyboardButton(
                "✅ Assign",
                callback_data=f"confirm:{session_id}"
            ),
            InlineKeyboardButton(
                "❌ Cancel",
                callback_data=f"cancel:{session_id}"
            ),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    employee_display = task["employee"]

    if employee_record and employee_record.get("employee_id"):
        employee_display = (
            f"{employee_record['name']} "
            f"({employee_record['employee_id']})"
        )

    reply = (
        "📋 Task Preview\n\n"
        f"Employee:\n{employee_display}\n\n"
        f"Task:\n{task['task']}\n\n"
        f"Deadline:\n{task['deadline']}\n\n"
        f"Priority:\n{task['priority']}\n\n"
        f"Summary:\n{task['summary']}\n\n"
        "Assign this task?"
    )

    if not employee_record:
        reply += (
            "\n\n⚠ Note:\n"
            "This employee was not found in employees.json.\n"
            "You may cancel and check the employee name."
        )
    elif not employee_record.get("telegram_chat_id"):
        reply += (
            "\n\n⚠ Note:\n"
            "This employee has no Telegram Chat ID in employees.json."
        )

    await update.message.reply_text(
        reply,
        reply_markup=reply_markup
    )


async def handle_employee_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    message: str
):
    chat_id = update.effective_chat.id
    employee = get_employee_by_chat_id(chat_id)

    if message.upper() == "DONE":
        await handle_employee_done(update, context, chat_id)
        return

    await forward_employee_message_to_boss(
        update=update,
        context=context,
        employee=employee,
        message=message
    )


async def handle_employee_done(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    chat_id: int
):
    result = engine.complete_task_by_chat_id(chat_id)

    if result["status"] != "completed":
        await update.message.reply_text(
            "⚠ I could not find an active assigned task for you.\n\n"
            "Please check with your boss."
        )
        return

    task = result["task"]
    employee = result["employee"]
    completed_at = get_time_text()

    await update.message.reply_text(
        "✅ Thank you.\n\n"
        "Your boss has been notified."
    )

    await send_boss_completion_notification(
        context=context,
        employee=employee,
        task=task,
        completed_at=completed_at
    )


async def forward_employee_message_to_boss(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    employee: dict,
    message: str
):
    boss_chat_id = get_boss_chat_id()

    if not boss_chat_id:
        await update.message.reply_text(
            "⚠ I received your message, but the Boss Chat ID is not configured."
        )
        return

    employee_name = employee.get("name", "Unknown employee")
    employee_id = employee.get("employee_id", "No employee ID")
    sent_at = get_time_text()

    boss_message = (
        "💬 Employee Reply\n\n"
        f"Employee:\n{employee_name} ({employee_id})\n\n"
        f"Message:\n{message}\n\n"
        f"Received at:\n{sent_at}"
    )

    try:
        await context.bot.send_message(
            chat_id=boss_chat_id,
            text=boss_message
        )

        await update.message.reply_text(
            "✅ Noted.\n\n"
            "I have forwarded your message to your boss.\n\n"
            "When the task is completed, reply:\n\n"
            "DONE"
        )

    except Exception as e:
        await update.message.reply_text(
            "⚠ I received your message but could not forward it to your boss.\n\n"
            f"Reason:\n{str(e)}"
        )


async def send_boss_completion_notification(
    context: ContextTypes.DEFAULT_TYPE,
    employee: dict,
    task: dict,
    completed_at: str
):
    boss_chat_id = get_boss_chat_id()

    if not boss_chat_id:
        return

    boss_message = (
        "✅ Task Completed\n\n"
        f"Employee:\n{employee['name']}\n\n"
        f"Task:\n{task['task']}\n\n"
        f"Completed at:\n{completed_at}"
    )

    await context.bot.send_message(
        chat_id=boss_chat_id,
        text=boss_message
    )


async def handle_unknown_user(update: Update):
    await update.message.reply_text(
        "You are not registered in this EVE system.\n\n"
        "Please contact your administrator.\n\n"
        "To see your Telegram Chat ID, type:\n\n"
        "ID"
    )


async def handle_confirmation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    chat_id = update.effective_chat.id

    if not is_boss(chat_id):
        await query.edit_message_text(
            "⚠ Only the Boss can assign or cancel tasks."
        )
        return

    try:
        action, session_id = query.data.split(":", 1)
    except ValueError:
        await query.edit_message_text(
            "⚠ Invalid action."
        )
        return

    if action == "confirm":
        await handle_assign_confirmation(query, context, session_id)
        return

    if action == "cancel":
        await handle_cancel_confirmation(query, session_id)
        return

    await query.edit_message_text(
        "⚠ Unknown action."
    )


async def handle_assign_confirmation(
    query,
    context: ContextTypes.DEFAULT_TYPE,
    session_id: str
):
    result = engine.confirm_task(session_id)

    if result["status"] != "assigned":
        await query.edit_message_text(result["message"])
        return

    task = result["task"]
    employee_record = result.get("employee_record")

    if not employee_record:
        await query.edit_message_text(
            "⚠ Task could not be sent.\n\n"
            "Employee was not found in employees.json.\n\n"
            "Please check the employee name and try again."
        )
        return

    if not employee_record.get("telegram_chat_id"):
        await query.edit_message_text(
            "⚠ Task could not be sent.\n\n"
            "Employee Telegram Chat ID is missing in employees.json."
        )
        return

    employee_message = (
        "📢 New Task\n\n"
        f"Task:\n{task['task']}\n\n"
        f"Deadline:\n{task['deadline']}\n\n"
        f"Priority:\n{task['priority']}\n\n"
        "You may reply with questions or updates.\n\n"
        "Reply:\n\n"
        "DONE\n\n"
        "when completed."
    )

    try:
        await context.bot.send_message(
            chat_id=employee_record["telegram_chat_id"],
            text=employee_message
        )
    except Exception as e:
        await query.edit_message_text(
            "⚠ Task was confirmed but could not be sent to the employee.\n\n"
            f"Reason:\n{str(e)}"
        )
        return

    await query.edit_message_text(
        f"✅ Task assigned to {employee_record['name']}.\n\n"
        "I will notify you once completed."
    )


async def handle_cancel_confirmation(query, session_id: str):
    result = engine.cancel_task(session_id)

    if result["status"] == "cancelled":
        await query.edit_message_text(
            "❌ Task cancelled.\n\n"
            "No employee message was sent."
        )
        return

    await query.edit_message_text(result["message"])


def run_bot():
    if not TELEGRAM_BOT_TOKEN:
        raise ValueError(
            "TELEGRAM_BOT_TOKEN is missing. Please update your .env file."
        )

    if not get_boss_chat_id():
        raise ValueError(
            "BOSS_CHAT_ID is missing. Please update your .env file."
        )

    app = Application.builder().token(
        TELEGRAM_BOT_TOKEN
    ).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(handle_confirmation))

    print(f"🚀 EVE v{EVE_VERSION} Telegram Bot is running...")

    app.run_polling()

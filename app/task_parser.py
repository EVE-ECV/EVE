"""
Task Parser

Converts a Boss's natural language instruction
into a structured Task object using the Local LLM.
"""

import json
from pathlib import Path

from app.llm import ask_llm
from app.models import Task


PROMPT_PATH = (
    Path(__file__).resolve().parent.parent
    / "prompts"
    / "task_prompt.txt"
)


def load_task_prompt() -> str:
    """
    Load the task parsing prompt.
    """

    if not PROMPT_PATH.exists():
        raise FileNotFoundError(
            f"Task prompt not found:\n{PROMPT_PATH}"
        )

    return PROMPT_PATH.read_text(
        encoding="utf-8"
    )


def create_fallback_task(reason: str) -> Task:
    """
    Return a safe fallback Task whenever parsing fails.
    """

    return Task(
        employee="Not specified",
        task="Unable to understand the instruction",
        deadline="Not specified",
        priority="Normal",
        summary=reason,
        confirmation_question=(
            "Please review or rewrite the instruction before assigning."
        )
    )


def parse_task(message: str) -> Task:
    """
    Convert a Boss instruction into a Task object.
    """

    if not message or not message.strip():
        return create_fallback_task(
            "The instruction is empty."
        )

    try:

        prompt_template = load_task_prompt()

        prompt = prompt_template.replace(
            "{message}",
            message.strip()
        )

        llm_response = ask_llm(prompt)

    except Exception as e:

        return create_fallback_task(
            f"Unable to contact the Local AI.\n\nReason: {str(e)}"
        )

    try:

        task_data = json.loads(
            llm_response
        )

    except json.JSONDecodeError:

        return create_fallback_task(
            "The Local AI returned an invalid JSON response."
        )

    required_fields = [
        "employee",
        "task",
        "deadline",
        "priority",
        "summary",
        "confirmation_question"
    ]

    for field in required_fields:

        if field not in task_data:

            task_data[field] = "Not specified"

    if not task_data["priority"]:
        task_data["priority"] = "Normal"

    try:

        return Task(
            **task_data
        )

    except Exception as e:

        return create_fallback_task(
            f"Unable to create Task object.\n\nReason: {str(e)}"
        )

"""
Data Models

Defines structured objects used by EVE.
"""

from pydantic import BaseModel


class Task(BaseModel):
    """
    Represents a task extracted from a boss message.
    """

    employee: str
    task: str
    deadline: str
    priority: str
    summary: str
    confirmation_question: str

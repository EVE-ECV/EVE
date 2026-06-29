"""
Data Models

Defines structured objects used throughout EVE.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Task(BaseModel):
    """
    Represents a task extracted from a Boss instruction.
    """

    # Core task details
    employee: str
    task: str
    deadline: str
    priority: str = "Normal"
    summary: str
    confirmation_question: str

    # Future-ready metadata
    task_id: Optional[str] = None
    status: str = "waiting_boss_confirmation"

    created_at: datetime = Field(default_factory=datetime.now)
    assigned_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    remarks: Optional[str] = None

    class Config:
        validate_assignment = True
        extra = "ignore"

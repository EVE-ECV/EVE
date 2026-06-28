"""
Task State Definitions

Defines the lifecycle of every task inside EVE.
"""

from enum import Enum


class TaskState(str, Enum):

    DRAFT = "draft"

    WAITING_BOSS_CONFIRMATION = "waiting_boss_confirmation"

    ASSIGNED = "assigned"

    ACCEPTED = "accepted"

    IN_PROGRESS = "in_progress"

    COMPLETED = "completed"

    REJECTED = "rejected"

    CANCELLED = "cancelled"

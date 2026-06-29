"""
Workflow Engine

Coordinates boss task creation, employee lookup,
confirmation sessions, task assignment, cancellation,
and employee completion.
"""

from app.task_parser import parse_task
from app.session import SessionManager
from app.employee_directory import EmployeeDirectory


class WorkflowEngine:

    def __init__(self):
        self.sessions = SessionManager()
        self.employee_directory = EmployeeDirectory()

    def process_message(self, message: str):
        """
        Process an incoming boss message and create
        a confirmation session.
        """

        if not message or not message.strip():
            return {
                "status": "error",
                "message": "Message is empty."
            }

        task = parse_task(message)

        employee_record = self.employee_directory.find_by_name(
            task.employee
        )

        session_id = self.sessions.create(task)

        return {
            "status": "waiting_boss_confirmation",
            "session_id": session_id,
            "original_message": message,
            "task": task.model_dump(),
            "employee_record": employee_record
        }

    def confirm_task(self, session_id: str):
        """
        Confirm a task and mark it as assigned.
        """

        session = self.sessions.get(session_id)

        if not session:
            return {
                "status": "error",
                "message": "Session not found."
            }

        task = session["task"]

        employee_record = self.employee_directory.find_by_name(
            task.employee
        )

        if not employee_record:
            return {
                "status": "error",
                "message": (
                    "Employee not found in employees.json. "
                    "Please check the employee name."
                )
            }

        if not employee_record.get("telegram_chat_id"):
            return {
                "status": "error",
                "message": (
                    "Employee Telegram Chat ID is missing in employees.json."
                )
            }

        self.sessions.update_state(
            session_id,
            "assigned"
        )

        return {
            "status": "assigned",
            "session_id": session_id,
            "task": task.model_dump(),
            "employee_record": employee_record
        }

    def cancel_task(self, session_id: str):
        """
        Cancel a task before assignment.
        """

        session = self.sessions.get(session_id)

        if not session:
            return {
                "status": "error",
                "message": "Session not found."
            }

        self.sessions.update_state(
            session_id,
            "cancelled"
        )

        return {
            "status": "cancelled",
            "session_id": session_id,
            "message": "Task cancelled."
        }

    def complete_task_by_chat_id(self, chat_id: int):
        """
        Mark the assigned task for a Telegram employee as completed.
        """

        employee_record = self.employee_directory.find_by_chat_id(
            chat_id
        )

        if not employee_record:
            return {
                "status": "error",
                "message": "Employee not found in directory."
            }

        employee_name = employee_record["name"]

        session_id, session = self.sessions.find_assigned_task_by_employee(
            employee_name
        )

        if not session:
            return {
                "status": "error",
                "message": "No assigned task found."
            }

        self.sessions.update_state(
            session_id,
            "completed"
        )

        return {
            "status": "completed",
            "session_id": session_id,
            "employee": employee_record,
            "task": session["task"].model_dump()
        }

    def get_employee_by_chat_id(self, chat_id: int):
        """
        Get employee record using Telegram Chat ID.
        """

        return self.employee_directory.find_by_chat_id(chat_id)

    def get_employee_by_name(self, name: str):
        """
        Get employee record using employee name.
        """

        return self.employee_directory.find_by_name(name)

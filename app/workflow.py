"""
Workflow Engine

Coordinates incoming messages, task parsing,
employee lookup, session creation, and workflow responses.
"""

from task_parser import parse_task
from session import SessionManager
from employee_directory import EmployeeDirectory


class WorkflowEngine:

    def __init__(self):
        self.sessions = SessionManager()
        self.employee_directory = EmployeeDirectory()

    def process_message(self, message: str):
        """
        Process an incoming boss message and create
        a confirmation session.
        """

        task = parse_task(message)

        employee_record = self.employee_directory.find(task.employee)

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
        employee_record = self.employee_directory.find(task.employee)

        self.sessions.update_state(session_id, "assigned")

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

        self.sessions.update_state(session_id, "cancelled")

        return {
            "status": "cancelled",
            "session_id": session_id
        }

"""
Workflow Engine

Coordinates the flow between incoming messages,
task parsing, and workflow responses.
"""

from task_parser import parse_task


class WorkflowEngine:

    def process_message(self, message: str):
        """
        Process an incoming boss message and return
        structured task information.
        """

        task = parse_task(message)

        return {
            "status": "parsed",
            "original_message": message,
            "task": task.model_dump()
        }

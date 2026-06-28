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

        task_result = parse_task(message)

        return {
            "status": "parsed",
            "original_message": message,
            "task_result": task_result
        }"""
Workflow Engine

Coordinates the flow between the Telegram bot,
task parser, and local LLM.
"""


class WorkflowEngine:

    def process_message(self, message: str):

        print("Received message:")

        print(message)

        return {
            "status": "received",
            "message": message
        }

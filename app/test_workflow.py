"""
Test Workflow

Allows users to test EVE without Telegram.
"""

from workflow import WorkflowEngine


def main():
    engine = WorkflowEngine()

    sample_message = "Ah Tan, please prepare the June sales report and send it to me by Friday."

    result = engine.process_message(sample_message)
    task = result["task"]

    print("Original Message:")
    print(result["original_message"])
    print("-" * 50)
    print("Parsed Task:")
    print(f"Employee              : {task['employee']}")
    print(f"Task                  : {task['task']}")
    print(f"Deadline              : {task['deadline']}")
    print(f"Priority              : {task['priority']}")
    print(f"Summary               : {task['summary']}")
    print(f"Confirmation Question : {task['confirmation_question']}")


if __name__ == "__main__":
    main()

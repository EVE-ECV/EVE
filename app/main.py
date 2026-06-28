"""
EVE

Application Entry Point
"""

from config import COMPANY_NAME, OLLAMA_MODEL
from workflow import WorkflowEngine


def main():
    print("=" * 50)
    print("EVE")
    print("The Local AI Operating System for SMEs")
    print("=" * 50)
    print(f"Built by      : {COMPANY_NAME}")
    print(f"Current Model : {OLLAMA_MODEL}")
    print("System started successfully.")
    print("-" * 50)

    sample_message = "Ah Tan, please prepare the June sales report and send it to me by Friday."

    engine = WorkflowEngine()
    result = engine.process_message(sample_message)

    print("Original Message:")
    print(result["original_message"])
    print("-" * 50)
    print("Parsed Task:")

    task = result["task"]

    print(f"Employee              : {task['employee']}")
    print(f"Task                  : {task['task']}")
    print(f"Deadline              : {task['deadline']}")
    print(f"Priority              : {task['priority']}")
    print(f"Summary               : {task['summary']}")
    print(f"Confirmation Question : {task['confirmation_question']}")


if __name__ == "__main__":
    main()"""
EVE

Application Entry Point
"""

from config import COMPANY_NAME, OLLAMA_MODEL
from workflow import WorkflowEngine


def main():
    print("=" * 50)
    print("EVE")
    print("The Local AI Operating System for SMEs")
    print("=" * 50)
    print(f"Built by      : {COMPANY_NAME}")
    print(f"Current Model : {OLLAMA_MODEL}")
    print("System started successfully.")
    print("-" * 50)

    sample_message = "Ah Tan, please prepare the June sales report and send it to me by Friday."

    engine = WorkflowEngine()
    result = engine.process_message(sample_message)

    print("Original Message:")
    print(result["original_message"])
    print("-" * 50)
    print("Parsed Task Result:")
    print(result["task_result"])


if __name__ == "__main__":
    main()

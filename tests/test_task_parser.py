"""
Tests for Task Parser.
"""

from app.task_parser import parse_task


def fake_llm_response(prompt: str) -> str:
    return """
{
  "employee": "Ah Tan",
  "task": "Prepare the June sales report",
  "deadline": "Friday",
  "priority": "Normal",
  "summary": "Ah Tan needs to prepare the June sales report by Friday.",
  "confirmation_question": "Do you want to assign this task to Ah Tan?"
}
"""


def test_parse_simple_task(monkeypatch):

    monkeypatch.setattr(
        "app.task_parser.ask_llm",
        fake_llm_response
    )

    task = parse_task(
        "Ask Ah Tan to prepare the June sales report by Friday."
    )

    assert task.employee == "Ah Tan"
    assert "June sales report" in task.task


def test_parser_returns_priority(monkeypatch):

    monkeypatch.setattr(
        "app.task_parser.ask_llm",
        fake_llm_response
    )

    task = parse_task(
        "Ask Ah Tan to prepare the June sales report."
    )

    assert task.priority == "Normal"


def test_parser_returns_summary(monkeypatch):

    monkeypatch.setattr(
        "app.task_parser.ask_llm",
        fake_llm_response
    )

    task = parse_task(
        "Ask Ah Tan to prepare the June sales report."
    )

    assert task.summary is not None

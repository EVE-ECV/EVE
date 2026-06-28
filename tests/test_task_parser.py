"""
Tests for Task Parser.
"""

from app.task_parser import parse_task


def test_parse_simple_task():

    task = parse_task(
        "Ask Ah Tan to prepare the June sales report by Friday."
    )

    assert task.employee == "Ah Tan"
    assert "June sales report" in task.task


def test_parser_returns_priority():

    task = parse_task(
        "Ask Ah Tan to prepare the June sales report."
    )

    assert task.priority is not None


def test_parser_returns_summary():

    task = parse_task(
        "Ask Ah Tan to prepare the June sales report."
    )

    assert task.summary is not None

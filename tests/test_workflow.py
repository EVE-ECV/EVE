"""
Tests for Workflow Engine.
"""

from app.workflow import WorkflowEngine


def test_confirm_unknown_session():
    engine = WorkflowEngine()

    result = engine.confirm_task("invalid-session-id")

    assert result["status"] == "error"


def test_cancel_unknown_session():
    engine = WorkflowEngine()

    result = engine.cancel_task("invalid-session-id")

    assert result["status"] == "error"

"""
Tests for Employee Directory.
"""

from app.employee_directory import EmployeeDirectory


def test_find_by_name():
    directory = EmployeeDirectory()

    employee = directory.find_by_name("Ah Tan")

    assert employee is not None
    assert employee["employee_id"] == "EMP001"


def test_find_by_chat_id():
    directory = EmployeeDirectory()

    employee = directory.find_by_chat_id(123456789)

    assert employee is not None
    assert employee["name"] == "Ah Tan"


def test_unknown_employee_returns_none():
    directory = EmployeeDirectory()

    employee = directory.find_by_name("Unknown Person")

    assert employee is None

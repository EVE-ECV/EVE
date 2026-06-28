"""
Employee Directory

Loads employees from data/employees.json
and allows EVE to look them up by name.
"""

import json
from pathlib import Path


class EmployeeDirectory:

    def __init__(self):
        data_file = (
            Path(__file__).parent.parent
            / "data"
            / "employees.json"
        )

        with open(data_file, "r", encoding="utf-8") as f:
            self.employees = json.load(f)

    def find(self, employee_name: str):

        employee = self.employees.get(
            employee_name.lower()
        )

        if employee is None:
            return None

        return employee

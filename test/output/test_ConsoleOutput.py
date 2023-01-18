import pytest

from model.Company import Company
from model.Employee import Employee
from output.ConsoleOutput import ConsoleOutput


@pytest.fixture
def company():
    emp1 = Employee(id=1, first_name="Jeff", manager=None, salary=10000)
    emp2 = Employee(id=2, first_name="Dave", manager=1, salary=10000)
    emp3 = Employee(id=4, first_name="Joanne", manager=2, salary=10000)
    emp4 = Employee(id=5, first_name="Carl", manager=4, salary=10000)
    emp5 = Employee(id=6, first_name="Lora", manager=5, salary=10000)
    emp6 = Employee(id=6, first_name="Jacob", manager=5, salary=10000)
    employeeData = [emp1, emp2, emp3, emp4, emp5, emp6]
    return Company(employeeData)


def test_display(company):
    ConsoleOutput.display(company)

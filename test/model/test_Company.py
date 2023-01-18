from model.Company import Company
from model.Employee import Employee
import pytest


@pytest.fixture
def company():
    emp1 = Employee(id=1, first_name="Jeff", manager=None, salary=10000)
    emp2 = Employee(id=2, first_name="Dave", manager=1, salary=10000)
    emp3 = Employee(id=4, first_name="Joanne", manager=2, salary=10000)
    emp4 = Employee(id=5, first_name="Carl", manager=4, salary=10000)
    emp5 = Employee(id=6, first_name="Lora", manager=5, salary=10000)
    emp6 = Employee(id=6, first_name="Jacob", manager=5, salary=10000)
    employeesData = [emp1, emp2, emp3, emp4, emp5, emp6]
    return Company(employeesData)


def test_setManagers(company):
    managers = company.managers
    assert len(managers) == 4

    # egde case: employeesData must contain manager
    emp7 = Employee(id=6, first_name="Jacob", manager=5, salary=10000)
    emp8 = Employee(id=7, first_name="Lora", manager=5, salary=10000)
    employeesData_withoutManagers = [emp7, emp8]
    with pytest.raises(ValueError):
        Company(employeesData_withoutManagers)


def test_setHierarchy(company):
    boss = company.hierarchy[0]
    assert boss.first_name == 'Jeff'  # fisrt element's manager must be None
    assert company.hierarchy[1].manager == boss.id  # logically correct

    # employeesData must contain boss
    with pytest.raises(ValueError):
        Company([Employee(id=5, first_name="Clare", manager=4, salary=0),
                 Employee(id=7, first_name="Lora", manager=5, salary=10000)])


def test_set_total_salary(company):
    salary = company.totalSalary
    assert salary == 60000

    # salary must greater than 0
    with pytest.raises(ValueError):
        Company([Employee(id=5, first_name="Clare", manager=4, salary=0),
                 Employee(id=7, first_name="Lora", manager=None, salary=10000),
                 Employee(id=8, first_name="Harry", manager=7, salary=10000)])

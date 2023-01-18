import pytest

from model.Employee import Employee, Manager


@pytest.fixture
def employeesData():
    emp1 = Employee(id=1, first_name="Jeff", manager=None, salary=10000)
    emp2 = Employee(id=2, first_name="Dave", manager=1, salary=10000)
    emp3 = Employee(id=4, first_name="Joanne", manager=2, salary=10000)
    emp4 = Employee(id=5, first_name="Carl", manager=4, salary=10000)
    emp5 = Employee(id=6, first_name="Lora", manager=5, salary=10000)
    emp6 = Employee(id=6, first_name="Jacob", manager=5, salary=10000)
    return [emp1, emp2, emp3, emp4, emp5, emp6]


def test_is_manager(employeesData):
    emp1 = Employee(id=1, first_name="Jeff", manager=None, salary=10000)
    assert emp1.is_manager(employeesData)


def test_set_employees(employeesData):
    manager = Manager(id=1, first_name="Jeff", manager=None, salary=10000)

    # empty_employeesData cannot be empty
    empty_employeesData = []
    with pytest.raises(ValueError):
        manager.setEmployees(empty_employeesData)

    # test if correct employee can be set to the manager
    manager.setEmployees(employeesData)
    assert manager.employees == ['Dave']

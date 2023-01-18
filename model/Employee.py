from pydantic import BaseModel, validator, Field
from typing import List, Optional, Set

from model.Role import Role


class Employee(Role, BaseModel):
    id: int = Field(gt=0)
    first_name: str = Field(min_length=2)
    manager: Optional[int]
    salary: int = Field(ge=0)
    roles: Set = set()

    @validator("first_name")
    def check_first_name(cls, first_name: str):
        if not first_name[0].isupper():
            raise ValueError("first letter of name must in uppercase")
        return first_name

    """ Check if an employee is manager from employeesData"""
    def is_manager(self, employeesData: List) -> bool:
        for employee in employeesData:
            if self.id is employee.manager:
                return True
        return False

    """ This method allows an employee to add multiple roles """
    def addRole(self, role: Role):
        self.roles.add(role)

    """ salary setter for employee """
    def setSalary(self, baseSalary: int):
        self.salary = baseSalary * 1


class Manager(Employee):
    employees: Set[str] = set()

    """ return a set of the manager's employee names """
    def employees(self):
        return self.employees

    """ Check if an employee is manager from employeesData,
     set all his employee names alphabetically """
    def setEmployees(self, employeesData: List):
        if not employeesData:
            raise ValueError("employeesData cannot be empty")
        employees = []
        for employee in employeesData:
            if self.id == employee.manager:
                employees.append(employee.first_name)
        employees.sort()
        self.employees = employees

    """ salary setter for manager """
    def setSalary(self, baseSalary: int):
        self.salary = baseSalary * 2

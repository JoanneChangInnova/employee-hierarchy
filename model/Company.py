from typing import List

from model import Employee


class Company:

    def __init__(self, employeesData):
        self.employeesData = employeesData
        self.managers = self.setManagers()
        self.hierarchy = self.setHierarchy()
        self.totalSalary = self.setTotalSalary()

    """ iterate through employeesData, find all managers in the company """
    def setManagers(self) -> List[Employee.Manager]:
        managers = []
        for employee in self.employeesData:
            if employee.is_manager(self.employeesData):
                manager = Employee.Manager(id=employee.id,
                                           first_name=employee.first_name,
                                           manager=employee.manager,
                                           salary=employee.salary)
                manager.setEmployees(self.employeesData)
                managers.append(manager)
        if not managers:
            raise ValueError("No managers found in the employeesData")
        return managers

    """ Set the company hierarchy by finding out boss first ( whose id
    is null ), then iterate through all managers, check whose manager
    is equal to previous manager's id."""
    def setHierarchy(self) -> List[Employee.Manager]:
        managers = self.managers
        hierarchy = []
        boss = list(filter(lambda m: m.manager is None, managers))
        if not boss:
            raise ValueError("No boss found in the employeesData")
        boss = boss[0]
        hierarchy.append(boss)
        i = 0
        current_manager = boss.id
        while i < len(managers):
            if managers[i].manager is current_manager:
                hierarchy.append(managers[i])
                current_manager = managers[i].id
                i = 0
            else:
                i = i + 1
        return hierarchy

    """ set total salary in the company from employeeData """
    def setTotalSalary(self) -> int:
        total_salary = 0
        for employee in self.employeesData:
            if employee.salary <= 0:
                raise ValueError("Invalid salary amount")
            total_salary += employee.salary
        return total_salary

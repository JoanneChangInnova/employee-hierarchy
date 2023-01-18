
from reader.EmployeeFile import EmployeeFile
from service.CompanyService import CompanyService


def test_importFile():
    file = EmployeeFile("../../resources/employees.json")
    CompanyService.importFile(file)

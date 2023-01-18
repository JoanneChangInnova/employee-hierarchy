from output.ConsoleOutput import ConsoleOutput
from reader.EmployeeFileReaderFactory import EmployeeFileReaderFactory

from model.Company import Company
from reader.EmployeeFile import EmployeeFile


class CompanyService:

    @classmethod
    def importFile(cls, file: EmployeeFile):
        reader = EmployeeFileReaderFactory.getFileReader(file)
        employeeData = reader.read()
        company = Company(employeeData)
        ConsoleOutput.display(company)

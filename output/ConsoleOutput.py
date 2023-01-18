
from model import Company
from output.Output import Output

""" Output Company data in console """


class ConsoleOutput(Output):

    @classmethod
    def display(cls, company: Company):
        for manager in company.hierarchy:
            print(manager.first_name)
            print(f'Employees of:{manager.first_name}')
            for emp in manager.employees:
                print(f'\t\t{emp}')
        print(f'\nTotal salary:{company.totalSalary}')

from service.CompanyService import CompanyService
from reader.EmployeeFile import EmployeeFile


def main():
    try:
        menu = input("Press 1 to use default file. Or press 2 to import file:")
        file = None
        if menu == "1":
            print("You chose default file")
            file = "resources/employees.json"
        elif menu == "2":
            file = input("Please import employee file:")
        else:
            print("You must choose between 1 or 2")

        if file:
            employeeFile = EmployeeFile(file)
            CompanyService.importFile(employeeFile)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

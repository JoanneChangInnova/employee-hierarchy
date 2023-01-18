import json
import os
import sys

import jsonschema
from jsonschema.validators import validate

from model import Employee
from reader.EmployeeFile import EmployeeFile
from reader.EmployeeFileReader import EmployeeFileReader


class JsonEmployeeFileReader(EmployeeFileReader):

    def __init__(self, file: EmployeeFile):
        self.file = file
        self.filePath = file.filePath
        self.employeeSchema = self.setEmployeeSchema()

    def setEmployeeSchema(self):
        LOCATE_PY_DIRECTORY_PATH = os.path.abspath(os.path.dirname(__file__))
        LOCATE_PY_PARENT_DIR = os.path.abspath(os.path.join(
            LOCATE_PY_DIRECTORY_PATH, ".."))
        return os.path.join(LOCATE_PY_PARENT_DIR,
                            "resources/employeeSchema.json")

    """ utility function for loading json file, throw exception when file
     not found """
    @staticmethod
    def loadFile(filePath):
        try:
            with open(filePath, "r") as read_file:
                return json.load(read_file)
        except FileNotFoundError as err:
            print(err)
            sys.exit(1)

    """ check if all the Employees in the given file are valid by
     validationSchema """
    def validateJson(self, inputPath):
        loadedSchema = self.loadFile(self.employeeSchema)
        loadedInput = self.loadFile(inputPath)
        try:
            validate(instance=loadedInput, schema=loadedSchema)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            return False
        except TypeError as err:
            print(err)
            return False
        return True

    """ load and validate the given file, return list of Employee
     instances"""
    def read(self):
        loadedFile = self.loadFile(self.filePath)
        isValid = self.validateJson(self.filePath)
        if isValid:
            try:
                return [Employee.Employee(**e) for e in loadedFile]
            except TypeError as err:
                print(err)
        else:
            raise ValueError("Invalid Employee data in file.")

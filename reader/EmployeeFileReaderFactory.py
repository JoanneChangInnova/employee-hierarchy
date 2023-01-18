from reader.EmployeeFile import EmployeeFile
from reader.JsonEmployeeFileReader import JsonEmployeeFileReader

""" This factory is used for creating new objects. 
We can use this to determine which FileReader gets
returned. """


class EmployeeFileReaderFactory:

    @classmethod
    def getFileReader(cls, file: EmployeeFile):
        if file.extension != '.json':
            raise ValueError("Invalid input file")
        return JsonEmployeeFileReader(file)

import os

""" This class encapsulates file info """


class EmployeeFile:

    def __init__(self, filePath: str):
        self.filePath = filePath
        self.extension = self.setExtension()

    def setExtension(self) -> str:
        extension = os.path.splitext(self.filePath)[1]
        if not extension:
            raise ValueError("Invalid filePath")
        return extension

from abc import ABC, abstractmethod

""" Base class for defining a file reader's behaviors """


class EmployeeFileReader(ABC):

    @abstractmethod
    def read(self):
        pass

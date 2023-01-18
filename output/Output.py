from abc import abstractmethod, ABC

""" Parent class for all output type (eg. ConsoleOutput/ FileOutput) """


class Output(ABC):

    @classmethod
    @abstractmethod
    def display(cls, company_data: dict):
        pass

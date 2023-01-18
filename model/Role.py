from abc import ABC, abstractmethod

""" An abstract class defines common behaviours of role """


class Role(ABC):
    """ According to different roles (eg, Employee, Manager)
        different salary rules can be set """

    @abstractmethod
    def setSalary(self):
        pass

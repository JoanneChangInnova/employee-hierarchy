import pytest

from reader.EmployeeFile import EmployeeFile
from reader.EmployeeFileReaderFactory import EmployeeFileReaderFactory
from reader.JsonEmployeeFileReader import JsonEmployeeFileReader


def test_getFileReader():
    # A jsonFileReader will be created by the factory when passing a json file
    file = EmployeeFile("test.json")
    assert isinstance(EmployeeFileReaderFactory.getFileReader(file),
                      JsonEmployeeFileReader)

    # other file type is not acceptable
    file = EmployeeFile("test.xlsx")
    with pytest.raises(ValueError):
        EmployeeFileReaderFactory.getFileReader(file)

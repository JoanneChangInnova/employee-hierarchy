import pytest

from reader.EmployeeFile import EmployeeFile


def test_setExtension():
    file = EmployeeFile("filePath.json")
    assert file.extension == ".json"
    with pytest.raises(ValueError):
        EmployeeFile("invalid/file/path")

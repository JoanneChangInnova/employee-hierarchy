
import pytest


from reader.EmployeeFile import EmployeeFile
from reader.JsonEmployeeFileReader import JsonEmployeeFileReader


@pytest.fixture
def jsonReader():
    return JsonEmployeeFileReader(EmployeeFile("../../resources/employees.json"))


def test_loadFile(jsonReader, capsys):
    jsonReader.loadFile("test/filePath")
    captured = capsys.readouterr()
    assert captured.out == "[Errno 2] No such file or directory: 'test/filePath'\n"


def test_validateJson(jsonReader):
    assert jsonReader.validateJson(jsonReader.filePath)


def test_read(jsonReader):
    jsonReader.read()

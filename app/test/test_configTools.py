import tools.configTools as configTools
import pytest

@pytest.mark.parametrize("countFormats, expected", [(1, True),
                                                    (0, False), 
                                                    (-1, True), 
                                                    (-10, False), 
                                                    ('1', False)])
def test_correctCountFormats(countFormats: int, expected: bool):
    actual = configTools.correctCountFormats(countFormats)

    assert actual == expected

@pytest.mark.parametrize("database_path, expected", [('test_DB.json', True), 
                                                     ('C:\\Users\\Максим\\Documents\\PythonProgram\\app\\test_DB.json', True), 
                                                     ('test_DB', False), 
                                                     ('C:\\Users\\Максим\\Documents\\PythonProgram\\app\\test_DB', False)])
def test_correctPath(database_path: str, expected: bool):
    actual = configTools.correctPath(database_path)

    assert actual == expected
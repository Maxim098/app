import tools.tools as tools
import pytest

@pytest.mark.parametrize("currentFormat, format, expected", [({'firstname': 'text', 'datebirth': 'date', 'email': 'email', 'phone': 'phone'}, {'name': 'test_format', 'firstname': 'text', 'datebirth': 'date', 'email': 'email', 'phone': 'phone'}, True), 
                                                     ({'date': 'date', 'msg': 'text'}, {'name': 'Заметка','date': 'date', 'msg': 'text'}, True), 
                                                     ({'msg': 'text'}, {'name': 'Заметка','date': 'date', 'msg': 'text'}, False), 
                                                     ({'date': 'date', 'msg': 'text', 'complexity': '5'}, {'name': 'Заметка','date': 'date', 'msg': 'text'}, True)])
def test_equalityFormats(currentFormat: dict[str: str], format: dict[str: str], expected: bool):
    actual = tools.equalityFormats(currentFormat, format)

    assert actual == expected

@pytest.mark.parametrize("options, expected", [({'name': 'test_format', 'firstname': 'Вася', 'datebirth': '20.12.2025', 'email': 'vasya@pukin.ru', 'phone': '+7 (123) 456 78 90'}, {'name': 'test_format', 'firstname': 'text', 'datebirth': 'date', 'email': 'email', 'phone': 'phone'}),
                                               ({'firstname': 'Вася', 'datebirth': '20.12.2025', 'email': 'vasya@pukin.ru', 'phone': '+7 (123) 456 78 90'}, {'firstname': 'text', 'datebirth': 'date', 'email': 'email', 'phone': 'phone'})])
def test_decodeInFormat(options: dict[str: str], expected: dict[str: str]):
    actual = tools.decodeInFormat(options)

    assert actual == expected

@pytest.mark.parametrize("options, expected", [(['--name=test', 'format', '--msg=1', '+', '1', '=', '2'], ['--name=test format', '--msg=1 + 1 = 2'])])
def test_correctsOptions(options: list[str], expected: list[str]):
    actual = tools.correctsOptions(options)

    assert actual == expected

@pytest.mark.parametrize("options, expected", [(['--name=test_format', '--firstname=Max', '--age=18'], True), 
                                               (['--name=msg', '--masg= 1 + 1 = 2'], True), 
                                               (['name=msg', '--masg= 1 + 1 = 2'], False), 
                                               (['--name msg', '--masg= 1 + 1 = 2'], False), 
                                               (['name msg', '--masg= 1 + 1 = 2'], False)])
def test_canDecodeInDict(options: list[str], expected: bool):
    actual = tools.canDecodeInDict(options)

    assert actual == expected

@pytest.mark.parametrize("options, expected", [(['--name=test_format', '--firstname=Max', '--age=18'], {'name': 'test_format', 'firstname': 'Max', 'age': '18'}), 
                                               (['--firstname=Max', '--age=18'], {'firstname': 'Max', 'age': '18'})])
def test_decodeInDict(options: list[str], expected: dict[str: str]):
    actual = tools.decodeInDict(options)

    assert actual == expected

@pytest.mark.parametrize("value, expected", [('19.12.2025', 'date'), 
                                             ('2025-12-19', 'date'), 
                                             ('+7 123 456 78 90', 'phone'),
                                             ('8 123 456 78 90', 'phone'),
                                             ('+7 (123) 456 78 90', 'phone'),
                                             ('a.bbb@ccc.ru', 'email'), 
                                             ('vasya@pukin.ru', 'email'),
                                             ('test msg', 'text'), 
                                             ('29.02.2025', 'text'), 
                                             ('8-444-444-44-44', 'text'), 
                                             ('vasyapukin.ru', 'text')])
def test_decodeInType(value: str, expected: str):
    actual = tools.decodeInType(value)

    assert actual == expected

@pytest.mark.parametrize("value, expected", [('19.12.2025', True), 
                                             ('2025-12-19', True), 
                                             ('2025.12.19', False),
                                             ('19-12-2025', False)])
def test_isDate(value: str, expected: bool):
    actual = tools.isDate(value)

    assert actual == expected

@pytest.mark.parametrize("year, mounth, day, expected", [(2025, 1, 1, True), 
                                                         (2025, 1, 31, True), 
                                                         (2024, 2, 1, True), 
                                                         (2024, 2, 29, True), 
                                                         (2025, 2, 1, True), 
                                                         (2025, 2, 29, False), 
                                                         (2025, 4, 1, True), 
                                                         (2025, 4, 30, True)])
def test_isCorrectDate(year: int, mounth: int, day: int, expected: bool):
    actual = tools.isCorrectDate(year, mounth, day)

    assert actual == expected

@pytest.mark.parametrize("value, expected", [('+7 123 456 78 90', True), 
                                             ('8 123 456 78 90', True), 
                                             ('8 (123) 456 78 90', True),
                                             ('9 123 456 78 90', False)])
def test_isPhone(value: str, expected: bool):
    actual = tools.isPhone(value)

    assert actual == expected

@pytest.mark.parametrize("value, expected", [('a.bbb@ccc.ru', True), 
                                             ('vasya@pukin.ru', True), 
                                             ('vasyapukin.ru', False)])
def test_isEmail(value: str, expected: bool):
    actual = tools.isEmail(value)

    assert actual == expected

@pytest.mark.parametrize("value, expected", [({'name': 'test', 'firstname': 'Max', 'age': '18'}, True), 
                                             ({'firstname': 'Max', 'age': '18'}, False)])
def test_formatHaveName(value: dict[str: str], expected: bool):
    actual = tools.formatHaveName(value)

    assert actual == expected
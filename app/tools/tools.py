import re

def equalityFormats(currentFormat: dict[str: str], format: dict[str: str]) -> bool:
    '''Сравнивает формат с найденым форматом'''

    format.pop('name')

    for key in currentFormat.keys():
        if key in format.keys():
            format.pop(key)

    return len(format) == 0

def decodeInFormat(options: dict[str: str]) -> dict[str: str]:
    '''Преобразует словарь параметров в формат для работы с базой данных'''

    for key in options.keys():
        if key == 'name':
            continue

        options[key] = decodeInType(options[key])
    
    return options

def correctsOptions(options: list[str]) -> list[str]:
    '''Поправляет переданные параметры при вызове в консоли'''
    i = 0

    while i != len(options) - 1:
        if re.fullmatch(r'^--\S+', options[i+1]) == None:
            options[i] += ' ' + options.pop(i+1)
            i -= 1

        i += 1

    return options

def canDecodeInDict(options: list[str]) -> bool:
    '''Проверяет все ли параметры имеют знак "="'''

    for option in options:
        if option[:2] != '--' or option.find('=') == -1:
            return False

    return True

def decodeInDict(options: list[str]) -> dict:
    '''Преобразует переданные параметры в словарь'''
    dict_ = dict()

    for option in options:
        key, value = option.split('=', 1)
        dict_[key[2:]] = value

    return dict_

def decodeInType(value: str) -> str:
    '''Возвращает тип данных значения'''

    if isDate(value):
        return 'date'
    elif isPhone(value):
        return 'phone'
    elif isEmail(value):
        return 'email'
    
    return 'text'

def isDate(value: str) -> bool:
    '''Проверяет является ли значение датой'''

    if re.fullmatch(r'\d{2}\.\d{2}\.\d{4}', value) != None:
        day, mounth, year = re.fullmatch(r'(\d{2})\.(\d{2})\.(\d{4})', value).groups()

        return isCorrectDate(int(year), int(mounth), int(day))
    elif re.fullmatch(r'\d{4}-\d{2}-\d{2}', value) != None:
        year, mounth, day = re.fullmatch(r'(\d{4})-(\d{2})-(\d{2})', value).groups()

        return isCorrectDate(int(year), int(mounth), int(day))
    
    return False

def isCorrectDate(year: int, mounth: int, day: int) -> bool:
    '''Проверяет правильность даты'''

    match mounth:
        case 2:
            if year % 100 != 0 and year % 4 == 0:
                if day > 0 and day <= 29:
                    return True
            else:
                if day > 0 and day <= 28:
                    return True
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            if day > 0 and day <= 31:
                return True
        case 4 | 6 | 9 | 11:
            if day > 0 and day <= 30:
                return True
        
    return False

def isPhone(value: str) -> bool:
    '''Проверяет является ли значение номером телефона'''

    return re.fullmatch(r'(\+7|8) \(?\d{3}\)? \d{3} \d{2} \d{2}', value) != None

def isEmail(value: str) -> bool:
    '''Проверяет является ли значение электронной почтой'''

    return re.fullmatch(r'[\w\.]+@[\w\.]+', value) != None

def formatHaveName(format: dict[str: str]) -> bool:
    '''Проверяет имеет ли формат для дабовления ключ "Name"'''

    return 'name' in format.keys()
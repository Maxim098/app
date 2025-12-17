import re
import click

def equalityFormats(format: dict, finded_format: dict) -> bool:
    finded_format_ = finded_format.copy()
    finded_format_.pop('name')

    if len(format) >= len(finded_format_):
        for key in format.keys():
            if finded_format_.get(key, None) == format[key]:
                finded_format_.pop(key)

        if len(finded_format_) == 0:
            return True

    return False

def haveName(dict_: dict) -> bool:
    return 'name' in dict_.keys()

def decodeInDict(lines: list) -> dict:
    lines = list(lines)
    dict_ = dict()
    step = 0

    while step != len(lines)-1:
        if str.find(lines[step+1], '=') == -1:
            lines[step] = str.join(' ', [lines[step], lines.pop(step+1)]) 
            step-=1

        step+=1

    for line in lines:
        key, value = line.split('=')
        dict_[key] = value

    return dict_
    #return dict(re.findall(r'([\w]+)=([\w\.@]+)', line))

def decodeInFormat(dict_: dict) -> dict:
    for key in dict_:
        dict_[key] = decodeInType(dict_[key])

    return dict_

def isCorrectType(line: str) -> bool:
    return line in ['date', 'phone', 'email', 'text']
        
def decodeInType(line: str) -> str:
    if isDate(line):
        return 'date'
    elif isPhone(line):
        return 'phone'
    elif isEmail(line):
        return 'email'
    
    return 'text'

def isDate(line: str) -> bool:
    if re.match(r'^\d{2}\.\d{2}\.\d{4}$', line):
        day, mounth, year = re.match(r'^(\d{2})\.(\d{2})\.(\d{4})$', line).groups()

        if isCorrectDate(day, mounth, year):
            return True

    elif re.match(r'^\d{4}-\d{2}-\d{2}$', line):
        year, mounth, day = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', line).groups()

        if isCorrectDate(day, mounth, year):
            return True

    return False
        
def isCorrectDate(day: str, mounth: str, year: str) -> bool:
    day = int(day)
    mounth = int(mounth)
    year = int(year)

    if mounth in [1, 3, 5, 7, 8, 10, 12]:
        if day >= 1 and day <= 31:
            return True
    if mounth in [4, 6, 11, 12]:
        if day >= 1 and day <= 30:
            return True
    if mounth == 2:
        if year % 4 == 0 and year % 100 != 0:
            if day >= 1 and day <= 29:
                return True
        else:
            if day >= 1 and day <= 28:
                return True

    return False    

def isPhone(line: str) -> bool:
    if re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', line):
        return True
    
    return False

def isEmail(line: str) -> bool:
    if re.match(r'^[\w\.-]+@[A-Za-z]+\.[A-Za-z]+$', line):
        return True
    
    return False
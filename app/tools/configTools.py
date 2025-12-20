import re

def correctCountFormats(countFormats: int) -> bool:
    '''Проверяет правильность настройки "countFormats"'''
    try:
        return countFormats >= 1 or countFormats == -1
    except Exception:
        return False
    
def correctPath(database_path: str) -> bool:
    '''Проверяет правильность настройки "database_path"'''

    return re.fullmatch(r'[А-Яа-яЁё\w\.\\:]+\.json', database_path) != None
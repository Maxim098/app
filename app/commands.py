from tools.tools import equalityFormats
from config import database_path, countFormats
from tinydb import TinyDB, Query
import re

def add_format(format: dict[str: str]):
    '''Добавляет формат в базу данных'''
    database = TinyDB(database_path)
    database.insert(format)

def get_format(format: dict[str: str]) -> (str | list[str] | dict[str: str]):
    '''Ищет переданный формат, при нахождении возвращает имена похожих форматов иначе возвращает формат обратно'''
    database = TinyDB(database_path)
    formats = database.search(Query().fragment(format))

    if len(formats) == 1:
        if equalityFormats(format.copy(), formats[0].copy()):
            return formats[0]['name']
    elif len(formats) >= 2:
        returnFormats = list()

        for format_ in formats:
            if len(returnFormats) < countFormats or countFormats == -1:
                if equalityFormats(format.copy(), format_.copy()):
                    returnFormats.append(format_['name'])

        if len(returnFormats) >=1:
            return returnFormats
        
    return format
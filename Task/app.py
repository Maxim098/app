from tools import decodeInDict, haveName, isCorrectType, decodeInFormat, equalityFormats
from config import path_DB
from tinydb import TinyDB, Query
import click

@click.group()
def commands():
    pass

@commands.command('get_format')
@click.argument('lines', nargs=-1)
def get_format(lines):
    dict_ = decodeInDict(lines)
    
    if haveName(dict_):
        click.echo('В форме не должно присутствовать поле "name"!')
    else:
        if len(dict_) < 2:
            click.echo('В форме должно быть минимум одно поле!')
        else:
            dict_format = decodeInFormat(dict_)
            db = TinyDB(path_DB)
            selected_dict = db.search(Query().fragment(dict_format))

            if len(selected_dict) == 0:
                click.echo(dict_format)
            elif len(selected_dict) == 1:
                if equalityFormats(dict_format, selected_dict[0]):
                    click.echo(selected_dict[0]['name'])
                else:
                    click.echo(dict_format)
            else:
                coincidences = False

                for format in selected_dict:
                    if equalityFormats(dict_format, selected_dict[0]):
                        click.echo(selected_dict[0]['name'])
                        coincidences = True

                if not coincidences:
                    click.echo(dict_format)

@commands.command('add_format')
@click.option('--name', 'name', type=click.STRING)
@click.argument('fields', nargs=-1)
def add_format(name: str, fields: list):
    dict_ = decodeInDict(fields)
    dict_['name'] = name

    if len(dict_) < 2:
        click.echo('В форме не должно быть только одно поле!')
    else:
        correct = True

        for i in range(len(dict_)):
            if list(dict_.keys())[i] == 'name':
                continue
            else:
                dict_[list(dict_.keys())[i]] = str.lower(list(dict_.values())[i])

                if not isCorrectType(list(dict_.values())[i]):
                    click.echo(f'В типе поля "{list(dict_.keys())[i]}" найдена ошибка! Тип поля может быть только: date, phone, email, text')
                    correct = False
        if correct:
            db = TinyDB(path_DB)
            db.insert(dict_)

if __name__ == "__main__":
    commands()
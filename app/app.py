from tools.tools import formatHaveName, decodeInDict, correctsOptions, canDecodeInDict, decodeInFormat
from tools.configTools import correctPath, correctCountFormats
from commands import add_format, get_format
import sys
import config

if __name__ == '__main__':
    options = sys.argv

    options.pop(0)

    if len(options) == 0:
        print('Отсутствует имя вызываемой функции и передоваемые ей параметры')
    elif len(options) == 1:
        print('Отсутствует имя вызываемой функции или передоваемые ей параметры')
    else:
        match options.pop(0):
            case 'add_format' | 'add-format':
                if not canDecodeInDict(correctsOptions(options)):
                    print('Неправильно переданны параметры')
                else:
                    format = decodeInDict(options)

                    if not formatHaveName(format):
                        print('При работе с функцией "add-format" параметр "name" должен присутствовать')
                    else:
                        if not correctPath(config.database_path):
                            print('Полный путь к базе данных некорректен')
                        else:
                            add_format(format)
            case 'get_format' | 'get-format':
                if not canDecodeInDict(correctsOptions(options)):
                    print('Неправильно переданны параметры')
                else:
                    format = decodeInFormat(decodeInDict(options))

                    if formatHaveName(format):
                        print('При работе с функцией "get-format" параметр "name" должен отсутствовать')
                    else:
                        if not correctPath(config.database_path):
                            print('Полный путь к базе данных некорректен')
                        elif not correctCountFormats(config.countFormats):
                            print('Количество показываемых форматов после выборки некорректны')
                        else:
                            print(get_format(format))
            case _:
                print('Вызываемая функция отсутствует или некорректна написана')
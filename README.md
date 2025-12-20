ИСПОЛЬЗОВАНИЕ

&emsp; Добавление данных:
&emsp;&emsp; python (__path__) [add_format | add-format] --name=(__name_format__) (__option__) [, ...]

&emsp;&emsp; __path__ - Полный путь к файлу app.py
&emsp;&emsp; __name_format__ - Название формата
&emsp;&emsp; __option__ - Передаваемый параметр в формате "--(__name_option__)=(__type__)"
&emsp;&emsp;&emsp;&emsp; __name_option__ - Название параметра
&emsp;&emsp;&emsp;&emsp; __type__ - Тип параметра (Тип может быть: date, phone, email, text)

&emsp;&emsp; Пример команды:
&emsp;&emsp;&emsp;&emsp; python C:\Users\Максим\Documents\PythonProgram\app\app.py add_format --name=Заметка --date=date --msg=text

&emsp; Выборка данных:
&emsp;&emsp; python (__path__) [get_format | get-format] (__option__) [, ...]

&emsp;&emsp; __path__ - Полный путь к файлу app.py
&emsp;&emsp; __option__ - Передаваемый параметр в формате "--(__name_option__)=(__value__)"
&emsp;&emsp;&emsp;&emsp; __name_option__ - Название параметра
&emsp;&emsp;&emsp;&emsp; __value__ - значение

&emsp;&emsp; Пример команды:
&emsp;&emsp;&emsp;&emsp; python C:\Users\Максим\Documents\PythonProgram\app\app.py get_format --date=date --msg=text

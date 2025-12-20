__О РАБОТЕ__ <br>
&emsp;&emsp; Функции для работы с базой данных tinydb

__МОДУЛИ__ <br>
&emsp;&emsp; В работе используется модуль: tinydb <br>
&emsp;&emsp; __pip install tinydb__

__ИСПОЛЬЗОВАНИЕ__ <br>
&emsp;&emsp; Добавление данных: <br>
&emsp;&emsp;&emsp;&emsp; python (__path__) [add_format | add-format] --name=(__name_format__) (__option__) [, ...]

&emsp;&emsp;&emsp;&emsp; __path__ - Полный путь к файлу app.py <br>
&emsp;&emsp;&emsp;&emsp; __name_format__ - Название формата <br>
&emsp;&emsp;&emsp;&emsp; __option__ - Передаваемый параметр в формате "--(__name_option__)=(__type__)" <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; __name_option__ - Название параметра <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; __type__ - Тип параметра (Тип может быть: date, phone, email, text) <br>

&emsp;&emsp;&emsp;&emsp; Пример команды: <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; __python C:\Users\Максим\Documents\PythonProgram\app\app.py add_format --name=Заметка --date=date --msg=text__

&emsp;&emsp; Выборка данных: <br>
&emsp;&emsp;&emsp;&emsp; python (__path__) [get_format | get-format] (__option__) [, ...] 

&emsp;&emsp;&emsp;&emsp; __path__ - Полный путь к файлу app.py <br>
&emsp;&emsp;&emsp;&emsp; __option__ - Передаваемый параметр в формате "--(__name_option__)=(__value__)" <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; __name_option__ - Название параметра <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; __value__ - значение <br>

&emsp;&emsp;&emsp;&emsp; Пример команды: <br>
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; __python C:\Users\Максим\Documents\PythonProgram\app\app.py get_format --date=date --msg=text__

__НАСТРОЙКИ__ <br>
&emsp;&emsp; __database_path__ - Полный путь к базе данных <br>
&emsp;&emsp; __countFormats__ - Количество найденых форматов показывать после выборки

# app

-------О Работе-------  
Сделана на python  
Работа выполняет задачу поиска шаблонов в Базе данных от tinyDB  

-------Используемые модули-------  
В работе используются python модули: click, tinyDB  
Их необходимо установить:  
pip install click  
pip install tinyDB  

-------Использование-------  
Команда get_format:  
&emsp;&emsp;  python (Полный путь к файлу app.py) get_format (Поля и его типы)  

&emsp;&emsp; Поле и его тип записываются в формате: key=value  
&emsp;&emsp;  Чтобы делать поиск по нескольким полям их надо разделить пробелом  
  
&emsp;&emsp;  Примеры использования команд:  
&emsp;&emsp;&emsp;&emsp;    python app.py get_format sender_phone=+7 111 222 33 44 recipient_phone=+7 555 666 77 88 msg=Ты пойдешь сегодня гулять?      
&emsp;&emsp;&emsp;&emsp;    python app.py get_format date=17.12.2025 msg=Помыть посуду!  
&emsp;&emsp;&emsp;&emsp;    python app.py get_format date_1=17.12.2025 date_2=20.12.2025  

&emsp;&emsp;  Итоги исользования команд:  
&emsp;&emsp;&emsp;&emsp;    (Название формы) При условии что есть форма с такими же полями  
&emsp;&emsp;&emsp;&emsp;    {fields_1: type, fields_2: type} Даёт форму которую вы хотели бы видеть в базе данных  

-------База данных-------  
В работе есть тестовая база данных, она содержит следующие формы:  
&emsp;&emsp;  name="Отправка сообщения"             sender_phone=phone   recipient_phone=phone   msg=text  
&emsp;&emsp;  name="Отправка письма"                sender_email=email   recipient_phone=email   msg=text  
&emsp;&emsp;  name="Заметка"                        date=date            msg=text  
&emsp;&emsp;  name="Диапазон дат"                   date_1=date          date_2=date  
&emsp;&emsp;  name="Данные пользователя"            firstname=text       lastname=text           email=email       date_birth=date  
&emsp;&emsp;  name="Данные о друге"                 firstname=text       lastname=text           date_birth=date  
&emsp;&emsp;  name="Заказ"                          product=text         arrival_date=date       order_date=date   email=email  
&emsp;&emsp;  name="Соединение строк"               line_1=text          line_2=text  
&emsp;&emsp;  name="Форма со всеми типами данных"   date=date            phone=phone             email=email       msg=text  
&emsp;&emsp;  name="ФИО"                            lastname=text        firstname=text          surname=text  

-------Файл настроек(config.py)-------  
path_DB - Полный путь к базе данных  
  

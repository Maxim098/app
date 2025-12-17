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
  python (Полный путь к файлу app.py) get_format (Поля и его типы)

  Поле и его тип записываются в формате: key=value
  Чтобы делать поиск по нескольким полям их надо разделить пробелом
  
  Примеры использования команд:
    python app.py get_format sender_phone=+7 111 222 33 44 recipient_phone=+7 555 666 77 88 msg=Ты пойдешь сегодня гулять?    
    python app.py get_format date=17.12.2025 msg=Помыть посуду!
    python app.py get_format date_1=17.12.2025 date_2=20.12.2025

  Итоги исользования команд:
    (Название формы) При условии что есть форма с такими же полями
    {fields_1: type, fields_2: type} Даёт форму которую вы хотели бы видеть в базе данных

-------База данных-------
В работе есть тестовая база данных, она содержит следующие формы:
  name="Отправка сообщения"             sender_phone=phone   recipient_phone=phone   msg=text
  name="Отправка письма"                sender_email=email   recipient_phone=email   msg=text
  name="Заметка"                        date=date            msg=text
  name="Диапазон дат"                   date_1=date          date_2=date
  name="Данные пользователя"            firstname=text       lastname=text           email=email       date_birth=date
  name="Данные о друге"                 firstname=text       lastname=text           date_birth=date
  name="Заказ"                          product=text         arrival_date=date       order_date=date   email=email
  name="Соединение строк"               line_1=text          line_2=text
  name="Форма со всеми типами данных"   date=date            phone=phone             email=email       msg=text
  name="ФИО"                            lastname=text        firstname=text          surname=text

-------Файл настроек(config.py)-------
path_DB - Полный путь к базе данных
  

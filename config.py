"""
config.py
---------

Этот файл содержит конфигурацию для подключения к базе данных.
Он используется для хранения параметров подключения в виде словаря `DATABASE_CONFIG`.

Переменные:
-----------
DATABASE_CONFIG : dict
    Словарь, содержащий параметры подключения к базе данных.

Ключи словаря DATABASE_CONFIG:
-------------------------------
host : str
    Адрес хоста базы данных.
database : str
    Имя базы данных.
user : str
    Имя пользователя для подключения к базе данных.
password : str
    Пароль пользователя для подключения к базе данных.

Пример использования:
---------------------
import mysql.connector
from config import DATABASE_CONFIG

connection = mysql.connector.connect(**DATABASE_CONFIG)
cursor = connection.cursor()
# Выполнение запросов к базе данных
cursor.close()
connection.close()
"""

DATABASE_CONFIG = {
    'host': '127.0.0.1',
    'database': 'project_220424_oskolkov',
    'user': 'root',
    'password': 'password'
}

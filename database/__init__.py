"""
database/__init__.py

Инициализация пакета базы данных.

Импортируемые модули:
----------------------
DatabaseManager: Класс для управления базой данных.

Примеры использования:
----------------------
from database import DatabaseManager

db_manager = DatabaseManager(db_config)
# Использование объекта db_manager для выполнения операций с базой данных.
"""
from .manager import DatabaseManager

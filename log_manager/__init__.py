"""
log_manager/__init__.py

Инициализация пакета логирования.

Импортируемые модули:
----------------------
QueryLogger: Класс для логирования запросов.

Примеры использования:
----------------------
from log_manager import QueryLogger

logger = QueryLogger()
# Использование объекта logger для логирования различных запросов и событий.
"""
from .logger import QueryLogger

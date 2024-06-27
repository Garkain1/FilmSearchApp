"""
authentication/__init__.py

Инициализация пакета аутентификации.

Импортируемые модули:
----------------------
AuthManager: Класс для управления аутентификацией пользователей.

Примеры использования:
----------------------
from authentication import AuthManager

auth_manager = AuthManager()
# Использование объекта auth_manager для регистрации и управления пользователями.
"""
from .manager import AuthManager

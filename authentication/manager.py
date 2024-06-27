"""
authentication/manager.py
--------------------------

Этот модуль содержит класс AuthManager, который используется для управления аутентификацией пользователей.
Он поддерживает регистрацию, вход, выход из системы и сохранение состояния пользователя.

Классы:
-------
AuthManager
    __init__(self, localization_manager, db_manager, state_file='user_state.json')
        Инициализирует объект AuthManager.

    register_user(self, username, password)
        Регистрирует нового пользователя с заданным именем пользователя и паролем.

    login_user(self, username, password)
        Выполняет вход пользователя с заданным именем пользователя и паролем.

    hash_password(self, password)
        Хэширует заданный пароль.

    logout_user(self)
        Выполняет выход пользователя из системы.

    save_state(self, username, hashed_password)
        Сохраняет состояние пользователя в файл.

    load_state(self)
        Загружает состояние пользователя из файла.

    check_user_exists(self, username, hashed_password)
        Проверяет, существует ли пользователь с заданным именем пользователя и хэшированным паролем.

    clear_state(self)
        Очищает состояние пользователя в файле.
"""

import hashlib
import json
import os


class AuthManager:
    """
    Класс для управления аутентификацией пользователей.

    Атрибуты:
    ----------
    localization_manager : LocalizationManager
        Объект для управления локализацией текстов.
    db_manager : DatabaseManager
        Объект для управления базой данных.
    state_file : str
        Путь к файлу состояния пользователя.
    user_id : int
        ID текущего пользователя (0, если не залогинен).
    username : bool
        Имя текущего пользователя (False, если не залогинен).

    Методы:
    -------
    __init__(self, localization_manager, db_manager, state_file='user_state.json')
        Инициализирует объект AuthManager.
    register_user(username, password)
        Регистрирует нового пользователя с заданным именем пользователя и паролем.
    login_user(username, password)
        Выполняет вход пользователя с заданным именем пользователя и паролем.
    hash_password(password)
        Хэширует заданный пароль.
    logout_user()
        Выполняет выход пользователя из системы.
    save_state(username, hashed_password)
        Сохраняет состояние пользователя в файл.
    load_state()
        Загружает состояние пользователя из файла.
    check_user_exists(username, hashed_password)
        Проверяет, существует ли пользователь с заданным именем пользователя и хэшированным паролем.
    clear_state()
        Очищает состояние пользователя в файле.
    """

    def __init__(self, localization_manager, db_manager, state_file='user_state.json'):
        """
        Инициализирует объект AuthManager.

        Параметры:
        ----------
        localization_manager : LocalizationManager
            Объект для управления локализацией текстов.
        db_manager : DatabaseManager
            Объект для управления базой данных.
        state_file : str, optional
            Путь к файлу состояния пользователя (по умолчанию 'user_state.json').
        """
        self.localization_manager = localization_manager
        self.db_manager = db_manager
        self.state_file = state_file
        self.user_id = 0
        self.username = False
        self.load_state()

    def register_user(self, username, password):
        """
        Регистрирует нового пользователя с заданным именем пользователя и паролем.

        Параметры:
        ----------
        username : str
            Имя пользователя.
        password : str
            Пароль пользователя.
        """
        while True:
            try:
                query_check = """
                SELECT COUNT(*) AS count FROM users WHERE username = %s
                """
                params_check = (username,)
                result_check = self.db_manager.execute_query(query_check, params_check)
                if result_check[0]['count'] > 0:
                    raise ValueError(self.localization_manager.get_localized_text('username_exists').format(username))

                hashed_password = self.hash_password(password)
                insert_query = """
                INSERT INTO users (username, password)
                VALUES (%s, %s)
                """
                params = (username, hashed_password)
                self.db_manager.execute_update(insert_query, params)
                self.login_user(username, password)
                break  # Выход из цикла при успешной регистрации
            except ValueError as e:
                print(e)
                choice = input(self.localization_manager.get_localized_text('try_again_prompt'))
                if choice.lower() == self.localization_manager.get_localized_text('back'):
                    break
                username = input(self.localization_manager.get_localized_text('enter_username'))
                password = input(self.localization_manager.get_localized_text('enter_password'))

    def login_user(self, username, password):
        """
        Выполняет вход пользователя с заданным именем пользователя и паролем.

        Параметры:
        ----------
        username : str
            Имя пользователя.
        password : str
            Пароль пользователя.

        Возвращает:
        ----------
        int
            ID пользователя при успешном входе.
        """
        hashed_password = self.hash_password(password)
        query = """
        SELECT id FROM users
        WHERE username = %s AND password = %s
        """
        params = (username, hashed_password)
        result = self.db_manager.execute_query(query, params)
        if result:
            self.user_id = result[0]['id']
            self.save_state(username, hashed_password)
            self.username = username
        return self.user_id

    @staticmethod
    def hash_password(password):
        """
        Хэширует заданный пароль.

        Параметры:
        ----------
        password : str
            Пароль пользователя.

        Возвращает:
        ----------
        str
            Хэшированный пароль.
        """
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return hashed_password

    def logout_user(self):
        """
        Выполняет выход пользователя из системы.
        """
        self.user_id = 0
        self.username = False
        self.clear_state()

    def save_state(self, username, hashed_password):
        """
        Сохраняет состояние пользователя в файл.

        Параметры:
        ----------
        username : str
            Имя пользователя.
        hashed_password : str
            Хэшированный пароль пользователя.
        """
        state = {
            'username': username,
            'hashed_password': hashed_password,
            'user_id': self.user_id
        }
        with open(self.state_file, 'w') as f:
            json.dump(state, f)

    def load_state(self):
        """
        Загружает состояние пользователя из файла.
        """
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                state = json.load(f)
                username = state.get('username')
                hashed_password = state.get('hashed_password')
                self.user_id = state.get('user_id', 0)
                if username and hashed_password:
                    if self.check_user_exists(username, hashed_password):
                        self.user_id = state['user_id']
                        self.username = state.get('username')
                    else:
                        self.user_id = 0
                        self.clear_state()

    def check_user_exists(self, username, hashed_password):
        """
        Проверяет, существует ли пользователь с заданным именем пользователя и хэшированным паролем.

        Параметры:
        ----------
        username : str
            Имя пользователя.
        hashed_password : str
            Хэшированный пароль пользователя.

        Возвращает:
        ----------
        bool
            True, если пользователь существует, иначе False.
        """
        query = """
        SELECT id FROM users
        WHERE username = %s AND password = %s
        """
        params = (username, hashed_password)
        result = self.db_manager.execute_query(query, params)
        return bool(result)

    def clear_state(self):
        """
        Очищает состояние пользователя в файле.
        """
        if os.path.exists(self.state_file):
            with open(self.state_file, 'w') as f:
                json.dump({'user_id': 0}, f)

"""
utils/localization.py
---------------------

Этот модуль содержит класс LocalizationManager,
который используется для управления локализацией текстов на разных языках.
Он поддерживает загрузку языковых пакетов из базы данных и файлов, а также их сохранение.

Классы:
-------
LocalizationManager
    __init__(self, language_file='language_pack.json')
        Инициализирует объект LocalizationManager.

    load_language_pack_from_database(self, language_code)
        Загружает языковой пакет из базы данных по заданному языковому коду.

    load_language_pack_from_file(self)
        Загружает языковой пакет из файла.

    save_language_pack_to_file(self)
        Сохраняет текущий языковой пакет в файл.

    get_localized_text(self, text_key)
        Возвращает локализованный текст по заданному ключу.

    change_language(self, new_language_code)
        Меняет текущий язык и загружает соответствующий языковой пакет из базы данных.

Функции:
--------
load_localization_texts_from_file(language_file='language_pack.json')
    Загружает тексты локализации из файла.
"""

import os
import json
import mysql.connector
from config import DATABASE_CONFIG


class LocalizationManager:
    """
    Класс для управления локализацией текстов на разных языках.

    Атрибуты:
    ----------
    language_file : str
        Путь к файлу языкового пакета.
    current_language_code : str
        Код текущего языка.
    localized_texts : dict
        Словарь локализованных текстов.

    Методы:
    -------
    __init__(self, language_file='language_pack.json')
        Инициализирует объект LocalizationManager.
    load_language_pack_from_database(language_code)
        Загружает языковой пакет из базы данных по заданному языковому коду.
    load_language_pack_from_file()
        Загружает языковой пакет из файла.
    save_language_pack_to_file()
        Сохраняет текущий языковой пакет в файл.
    get_localized_text(text_key)
        Возвращает локализованный текст по заданному ключу.
    change_language(new_language_code)
        Меняет текущий язык и загружает соответствующий языковой пакет из базы данных.
    """

    def __init__(self, language_file='language_pack.json'):
        """
        Инициализирует объект LocalizationManager.

        Параметры:
        ----------
        language_file : str, optional
            Путь к файлу языкового пакета (по умолчанию 'language_pack.json').
        """
        self.language_file = language_file
        self.current_language_code = None
        self.localized_texts = {}

        if os.path.exists(self.language_file):
            self.load_language_pack_from_file()
        else:
            self.load_language_pack_from_database('en')
            self.save_language_pack_to_file()

    def load_language_pack_from_database(self, language_code):
        """
        Загружает языковой пакет из базы данных по заданному языковому коду.

        Параметры:
        ----------
        language_code : str
            Код языка для загрузки языкового пакета.
        """
        try:
            connection = mysql.connector.connect(**DATABASE_CONFIG)
            cursor = connection.cursor(dictionary=True)

            query = """
            SELECT lt.text_key, lt.text_value
            FROM localized_text lt
            JOIN language_pack lp ON lt.language_id = lp.language_id
            WHERE lp.language_code = %s
            """
            cursor.execute(query, (language_code,))
            localized_texts = cursor.fetchall()

            self.localized_texts = {text['text_key']: text['text_value'] for text in localized_texts}
            self.current_language_code = language_code

            cursor.close()
            connection.close()

        except mysql.connector.Error as error:
            print(f"Error loading language pack from database: {error}")

    def load_language_pack_from_file(self):
        """
        Загружает языковой пакет из файла.
        """
        if os.path.exists(self.language_file):
            with open(self.language_file, 'r', encoding='utf-8') as f:
                self.localized_texts = json.load(f)
                self.current_language_code = self.localized_texts.get('_meta', {}).get('current_language_code', None)
        else:
            print(f"Language file '{self.language_file}' not found. Creating a new one.")

    def save_language_pack_to_file(self):
        """
        Сохраняет текущий языковой пакет в файл.
        """
        try:
            with open(self.language_file, 'w', encoding='utf-8') as f:
                json.dump(self.localized_texts, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving language pack to file: {e}")

    def get_localized_text(self, text_key):
        """
        Возвращает локализованный текст по заданному ключу.

        Параметры:
        ----------
        text_key : str
            Ключ локализованного текста.

        Возвращает:
        ----------
        str
            Локализованный текст.
        """
        return self.localized_texts.get(text_key, f'[{text_key}]')

    def change_language(self, new_language_code):
        """
        Меняет текущий язык и загружает соответствующий языковой пакет из базы данных.

        Параметры:
        ----------
        new_language_code : str
            Код нового языка для загрузки языкового пакета.
        """
        if new_language_code != self.current_language_code:
            self.load_language_pack_from_database(new_language_code)

            self.localized_texts['_meta'] = {'current_language_code': new_language_code}
            self.save_language_pack_to_file()


def load_localization_texts_from_file(language_file='language_pack.json'):
    """
    Загружает тексты локализации из файла.

    Параметры:
    ----------
    language_file : str, optional
        Путь к файлу языкового пакета (по умолчанию 'language_pack.json').

    Возвращает:
    ----------
    LocalizationManager
        Объект LocalizationManager с загруженными текстами локализации.
    """
    localization_manager = LocalizationManager(language_file)
    return localization_manager

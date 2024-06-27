"""
log_manager/logger.py
-----------------------

Этот модуль содержит класс QueryLogger,который используется для ведения журнала поисковых запросов пользователей
в базе данных и получения популярных поисковых запросов.

Классы:
-------
QueryLogger
    __init__(self)
        Инициализирует объект QueryLogger.

    connect(self)
        Устанавливает соединение с базой данных.

    disconnect(self)
        Закрывает соединение с базой данных.

    log_keyword_search(self, user_id, keywords)
        Записывает запрос поиска по ключевым словам.

    log_genre_search(self, user_id, genre)
        Записывает запрос поиска по жанру.

    log_year_search(self, user_id, year)
        Записывает запрос поиска по году.

    log_actor_search(self, user_id, actor)
        Записывает запрос поиска по актеру.

    log_multiple_criteria_search(self, user_id, keywords, genre, start_year, end_year, actor)
        Записывает запрос поиска по нескольким критериям.

    log_query(self, user_id, search_type, params)
        Записывает поисковый запрос в базу данных.

    get_popular_search_queries(self, limit=10)
        Получает популярные поисковые запросы.

    __del__(self)
        Закрывает соединение с базой данных при удалении объекта.
"""

import mysql.connector
import json
from config import DATABASE_CONFIG


class QueryLogger:
    """
    Класс для ведения журнала поисковых запросов пользователей.

    Методы:
    -------
    __init__(self)
        Инициализирует объект QueryLogger.
    connect(self)
        Устанавливает соединение с базой данных.
    disconnect(self)
        Закрывает соединение с базой данных.
    log_keyword_search(self, user_id, keywords)
        Записывает запрос поиска по ключевым словам.
    log_genre_search(self, user_id, genre)
        Записывает запрос поиска по жанру.
    log_year_search(self, user_id, year)
        Записывает запрос поиска по году.
    log_actor_search(self, user_id, actor)
        Записывает запрос поиска по актеру.
    log_multiple_criteria_search(self, user_id, keywords, genre, start_year, end_year, actor)
        Записывает запрос поиска по нескольким критериям.
    log_query(self, user_id, search_type, params)
        Записывает поисковый запрос в базу данных.
    get_popular_search_queries(self, limit=10)
        Получает популярные поисковые запросы.
    __del__(self)
        Закрывает соединение с базой данных при удалении объекта.
    """

    def __init__(self):
        """
        Инициализирует объект QueryLogger.
        """
        self.connection = None
        self.cursor = None

    def connect(self):
        """
        Устанавливает соединение с базой данных.
        """
        self.connection = mysql.connector.connect(**DATABASE_CONFIG)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        """
        Закрывает соединение с базой данных.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def log_keyword_search(self, user_id, keywords):
        """
        Записывает запрос поиска по ключевым словам.

        Параметры:
        ----------
        user_id : int
            ID пользователя.
        keywords : str
            Ключевые слова для поиска.
        """
        self.log_query(user_id, "keyword", {"keywords": keywords})

    def log_genre_search(self, user_id, genre):
        """
        Записывает запрос поиска по жанру.

        Параметры:
        ----------
        user_id : int
            ID пользователя.
        genre : str
            Жанр для поиска.
        """
        self.log_query(user_id, "genre", {"genre": genre})

    def log_year_search(self, user_id, year):
        """
        Записывает запрос поиска по году.

        Параметры:
        ----------
        user_id : int
            ID пользователя.
        year : int
            Год для поиска.
        """
        self.log_query(user_id, "year", {"year": year})

    def log_actor_search(self, user_id, actor):
        """
        Записывает запрос поиска по актеру.

        Параметры:
        ----------
        user_id : int
            ID пользователя.
        actor : str
            Имя актера для поиска.
        """
        self.log_query(user_id, "actor", {"actor": actor})

    def log_multiple_criteria_search(self, user_id, keywords, genre, start_year, end_year, actor):
        """
        Записывает запрос поиска по нескольким критериям.

        Параметры:
        ----------
        user_id : int
            ID пользователя.
        keywords : list
            Список ключевых слов для поиска.
        genre : str
            Жанр для поиска.
        start_year : int
            Начальный год для поиска.
        end_year : int
            Конечный год для поиска.
        actor : str
            Имя актера для поиска.
        """
        self.log_query(user_id, "actor", {"keywords": keywords, "genre": genre,
                                          "start_year": start_year, "end_year": end_year, "actor": actor, })

    def log_query(self, user_id, search_type, params):
        """
        Записывает поисковый запрос в базу данных.

        Параметры:
        ----------
        user_id : int
            ID пользователя.
        search_type : str
            Тип поиска (ключевое слово, жанр, год и т.д.).
        params : dict
            Параметры поиска.
        """
        if not self.connection:
            self.connect()

        insert_query = """
        INSERT INTO user_queries (user_id, search_type, search_params)
        VALUES (%s, %s, %s)
        """
        params = (user_id, search_type, json.dumps(params))
        self.cursor.execute(insert_query, params)
        self.connection.commit()

    def get_popular_search_queries(self, limit=10):
        """
        Получает популярные поисковые запросы.

        Параметры:
        ----------
        limit : int, optional
            Максимальное количество популярных запросов для получения (по умолчанию 10).

        Возвращает:
        ----------
        list
            Список популярных поисковых запросов.
        """
        if not self.connection:
            self.connect()

        query = """
SELECT search_type, search_params, COUNT(*) AS query_count
FROM user_queries
GROUP BY search_type, search_params
ORDER BY query_count DESC
        LIMIT %s
        """
        params = (limit,)
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def __del__(self):
        """
        Закрывает соединение с базой данных при удалении объекта.
        """
        self.disconnect()

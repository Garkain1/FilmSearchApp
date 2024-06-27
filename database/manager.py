"""
database/manager.py
--------------------

Этот модуль содержит класс DatabaseManager, который используется для управления подключением к базе данных MySQL
и выполнения различных SQL-запросов для поиска фильмов.

Класс:
------
DatabaseManager
    __init__(self, host, user, password, database)
        Инициализирует объект DatabaseManager.

    connect(self)
        Устанавливает соединение с базой данных.

    disconnect(self)
        Закрывает соединение с базой данных.

    get_random_movies(self, limit=10)
        Возвращает случайные фильмы из базы данных.

    execute_query(self, query, params=None)
        Выполняет SQL-запрос и возвращает результаты.

    fetch_column(self, table_name, column_name)
        Возвращает все значения указанного столбца из указанной таблицы.

    execute_update(self, query, params=None)
        Выполняет SQL-запрос на обновление данных.

    search_movies(self, keywords=None, genre=None, start_year=None,
                  end_year=None, actor_name=None, sort_by=None, sort_order="ASC")
        Ищет фильмы в базе данных по заданным критериям.
"""

import mysql.connector


class DatabaseManager:
    """
    Класс для управления базой данных MySQL.

    Атрибуты:
    ----------
    host : str
        Адрес хоста базы данных.
    user : str
        Имя пользователя для подключения к базе данных.
    password : str
        Пароль для подключения к базе данных.
    database : str
        Название базы данных.
    connection : mysql.connector.connection.MySQLConnection
        Объект подключения к базе данных.
    cursor : mysql.connector.cursor.MySQLCursor
        Объект курсора для выполнения SQL-запросов.

    Методы:
    -------
    connect()
        Устанавливает соединение с базой данных.
    disconnect()
        Закрывает соединение с базой данных.
    get_random_movies(limit=10)
        Возвращает случайные фильмы из базы данных.
    execute_query(query, params=None)
        Выполняет SQL-запрос и возвращает результаты.
    fetch_column(table_name, column_name)
        Возвращает все значения указанного столбца из указанной таблицы.
    execute_update(query, params=None)
        Выполняет SQL-запрос на обновление данных.
    search_movies(keywords=None, genre=None, start_year=None, end_year=None,
                  actor_name=None, sort_by=None, sort_order="ASC")
        Ищет фильмы в базе данных по заданным критериям.
    """

    def __init__(self, host, user, password, database):
        """
        Инициализирует объект DatabaseManager.

        Параметры:
        ----------
        host : str
            Адрес хоста базы данных.
        user : str
            Имя пользователя для подключения к базе данных.
        password : str
            Пароль для подключения к базе данных.
        database : str
            Название базы данных.
        """
        self.cursor = None
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """
        Устанавливает соединение с базой данных.
        """
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def disconnect(self):
        """
        Закрывает соединение с базой данных.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def get_random_movies(self, limit=10):
        """
        Возвращает случайные фильмы из базы данных.

        Параметры:
        ----------
        limit : int, optional
            Количество фильмов для возврата (по умолчанию 10).

        Возвращает:
        ----------
        list of dict
            Список случайных фильмов.
        """
        query = """WITH film_details AS (
    SELECT 
        f.title AS title,
        f.description AS description,
        c.name AS genre,
        f.release_year AS release_year,
        GROUP_CONCAT(DISTINCT CONCAT(a.first_name, ' ', a.last_name) SEPARATOR ', ') AS actors
    FROM film f
    LEFT JOIN film_category fc ON f.film_id = fc.film_id
    LEFT JOIN category c ON fc.category_id = c.category_id
    LEFT JOIN film_actor fa ON f.film_id = fa.film_id
    LEFT JOIN actor a ON fa.actor_id = a.actor_id
    GROUP BY f.film_id, f.title, f.description, c.name, f.release_year
)
SELECT *
FROM film_details
ORDER BY RAND() LIMIT %s"""
        params = (limit,)
        return self.execute_query(query, params)

    def execute_query(self, query, params=None):
        """
        Выполняет SQL-запрос и возвращает результаты.

        Параметры:
        ----------
        query : str
            SQL-запрос для выполнения.
        params : tuple, optional
            Параметры для SQL-запроса.

        Возвращает:
        ----------
        list of dict
            Результаты выполнения SQL-запроса.
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_column(self, table_name, column_name):
        """
        Возвращает все значения указанного столбца из указанной таблицы.

        Параметры:
        ----------
        table_name : str
            Название таблицы.
        column_name : str
            Название столбца.

        Возвращает:
        ----------
        list
            Список значений указанного столбца.
        """
        column = []
        cursor = self.connection.cursor()
        query = f"SELECT {column_name} FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            column.append(row[0])
        return column

    def execute_update(self, query, params=None):
        """
        Выполняет SQL-запрос на обновление данных.

        Параметры:
        ----------
        query : str
            SQL-запрос для выполнения.
        params : tuple, optional
            Параметры для SQL-запроса.
        """
        self.cursor.execute(query, params)
        self.connection.commit()

    def search_movies(self, keywords=None, genre=None, start_year=None, end_year=None,
                      actor_name=None, sort_by=None, sort_order="ASC"):
        """
        Ищет фильмы в базе данных по заданным критериям.

        Параметры:
        ----------
        keywords : list of str, optional
            Ключевые слова для поиска по названию фильма.
        genre : str, optional
            Жанр фильма.
        start_year : int, optional
            Начальный год выпуска фильма.
        end_year : int, optional
            Конечный год выпуска фильма.
        actor_name : str, optional
            Имя актера для поиска.
        sort_by : str, optional
            Поле для сортировки результатов.
        sort_order : str, optional
            Порядок сортировки ("ASC" или "DESC").

        Возвращает:
        ----------
        list of dict
            Результаты поиска фильмов.
        """
        base_query = """WITH film_details AS (
    SELECT 
        f.title AS title,
        f.description AS description,
        c.name AS genre,
        f.release_year AS release_year,
        GROUP_CONCAT(DISTINCT CONCAT(a.first_name, ' ', a.last_name) SEPARATOR ', ') AS actors
    FROM film f
    LEFT JOIN film_category fc ON f.film_id = fc.film_id
    LEFT JOIN category c ON fc.category_id = c.category_id
    LEFT JOIN film_actor fa ON f.film_id = fa.film_id
    LEFT JOIN actor a ON fa.actor_id = a.actor_id
    GROUP BY f.film_id, f.title, f.description, c.name, f.release_year
)
SELECT *
FROM film_details
WHERE 1=1"""
        params = []

        if keywords:
            keyword_conditions = " OR ".join(["title LIKE %s"] * len(keywords))
            base_query += f" AND ({keyword_conditions})"
            for keyword in keywords:
                params.append(f"%{keyword}%")

        if genre:
            base_query += " AND genre = %s"
            params.append(genre)

        if start_year:
            base_query += " AND release_year >= %s"
            params.append(start_year)

        if end_year:
            base_query += " AND release_year <= %s"
            params.append(end_year)

        if actor_name:
            base_query += " AND actors LIKE %s"
            params.append(f"%{actor_name}%")

        if sort_by:
            base_query += f" ORDER BY {sort_by} {sort_order}"

        base_query += f" LIMIT 10"

        self.cursor.execute(base_query, params)
        return self.cursor.fetchall()

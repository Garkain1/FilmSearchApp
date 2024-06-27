"""
film_search_app.py
------------------

Этот файл реализует приложение для поиска фильмов с использованием базы данных.
Приложение предлагает пользователю различные функции, такие как регистрация, вход в систему,
поиск фильмов по различным критериям, вывод популярных запросов и изменение языка интерфейса.

Классы:
-------
FilmSearchApp:
    Основной класс приложения для поиска фильмов.

Модули:
-------
Импортируемые модули, необходимые для работы приложения:
- DatabaseManager из database
- AuthManager из authentication
- load_localization_texts_from_file из utils
- QueryLogger из log_manager
- json

Переменные:
-----------
Некоторые переменные, которые используются в классе:
- db_config: Конфигурация базы данных
- language_file: Файл с текстами локализации (по умолчанию 'language_pack.json')
- state_file: Файл состояния пользователя (по умолчанию 'user_state.json')

Методы:
-------
- __init__(self, db_config, language_file='language_pack.json', state_file='user_state.json'):
    Инициализация приложения, загрузка конфигураций, создание менеджеров и установка состояния.

- start(self):
    Начало работы приложения, устанавливает соединение с базой данных и запускает главное меню.

- run_main_menu(self):
    Запуск главного меню, которое отображает пользователю опции и обрабатывает их выбор.

- get_chunks(lst, chunk_size):
    Статический метод для разбиения списка на куски заданного размера.

- display_menu(self):
    Отображение главного меню с различными опциями, включая смену языка и текущее состояние пользователя.

- user_display(self):
    Отображение информации о текущем пользователе, включая его идентификатор и имя.

- app_exit(self):
    Выход из приложения, отключение от базы данных и очистка данных.

- process_choice(self, choice):
    Обработка выбора пользователя из главного меню: вызов соответствующей функции в зависимости от выбора.

- search_movies_by_keyword(self):
    Поиск фильмов по ключевым словам.

- search_movies_by_genre(self):
    Поиск фильмов по жанру.

- search_movies_by_year(self):
    Поиск фильмов по году выпуска.

- search_movies_by_actor(self):
    Поиск фильмов по актерам.

- search_movies_by_multiple_criteria(self):
    Поиск фильмов по нескольким критериям: ключевым словам, жанру, году выпуска, актеру.

- display_popular_search_queries(self):
    Отображение популярных поисковых запросов, сохраненных в логах.

- register_user(self):
    Регистрация нового пользователя в системе.

- login_user(self):
    Вход пользователя в систему.

- logout_user(self):
    Выход пользователя из системы.

- change_language(self):
    Изменение языка интерфейса приложения.

- select_language(self):
    Выбор нового языка интерфейса из доступных опций.

- display_results(self, results=None):
    Отображение результатов поиска фильмов в форматированном виде.

Примечания:
-----------
- Приложение использует различные модули для работы с базой данных, аутентификации,
  локализацией и логированием запросов.
- Оно предоставляет удобный интерфейс для пользователя с поддержкой различных языков через файлы локализации.
- Класс `FilmSearchApp` организует весь функционал в удобный и легко расширяемый интерфейс поиска фильмов.
"""

from database import DatabaseManager
from authentication import AuthManager
from utils import load_localization_texts_from_file
from log_manager import QueryLogger
import json


class FilmSearchApp:
    """
    Основной класс приложения для поиска фильмов.

    Методы:
    -------
    - __init__(self, db_config, language_file='language_pack.json', state_file='user_state.json'):
        Инициализация приложения, загрузка конфигураций, создание менеджеров и установка состояния.

    - start(self):
        Начало работы приложения, устанавливает соединение с базой данных и запускает главное меню.

    - run_main_menu(self):
        Запуск главного меню, которое отображает пользователю опции и обрабатывает их выбор.

    - get_chunks(lst, chunk_size):
    Статический метод для разбиения списка на куски заданного размера.

    - display_menu(self):
        Отображение главного меню с различными опциями, включая смену языка и текущее состояние пользователя.

    - user_display(self):
        Отображение информации о текущем пользователе, включая его идентификатор и имя.

    - app_exit(self):
        Выход из приложения, отключение от базы данных и очистка данных.

    - process_choice(self, choice):
        Обработка выбора пользователя из главного меню: вызов соответствующей функции в зависимости от выбора.

    - search_movies_by_keyword(self):
        Поиск фильмов по ключевым словам.

    - search_movies_by_genre(self):
        Поиск фильмов по жанру.

    - search_movies_by_year(self):
        Поиск фильмов по году выпуска.

    - search_movies_by_actor(self):
        Поиск фильмов по актерам.

    - search_movies_by_multiple_criteria(self):
        Поиск фильмов по нескольким критериям: ключевым словам, жанру, году выпуска, актерам.

    - display_popular_search_queries(self):
        Отображение популярных поисковых запросов, сохраненных в логах.

    - register_user(self):
        Регистрация нового пользователя в системе.

    - login_user(self):
        Вход пользователя в систему.

    - logout_user(self):
        Выход пользователя из системы.

    - change_language(self):
        Изменение языка интерфейса приложения.

    - select_language(self):
        Выбор нового языка интерфейса из доступных опций.

    - display_results(self, results=None):
        Отображение результатов поиска фильмов в форматированном виде.
    """

    def __init__(self, db_config, language_file='language_pack.json', state_file='user_state.json'):
        """
        Инициализация приложения, загрузка конфигураций, создание менеджеров и установка состояния.

        Параметры:
        ----------
        - db_config: dict
            Конфигурация базы данных.
        - language_file: str
            Файл с текстами локализации (по умолчанию 'language_pack.json').
        - state_file: str
            Файл состояния пользователя (по умолчанию 'user_state.json').
        """
        self.localization_manager = load_localization_texts_from_file(language_file)
        self.db_manager = DatabaseManager(**db_config)
        self.db_manager.connect()
        self.auth_manager = AuthManager(self.localization_manager, self.db_manager, state_file)
        self.result = self.display_results(self.db_manager.get_random_movies())
        self.query_logger = QueryLogger()
        self.db_manager.disconnect()
        self.header = '''+----------------------------------------------------------+
|   _____ _             __  __               _             |  
|  |_   _| |__   ___   |  \/  | ___ __    __(_) ___  ___   |
|    | | | '_ \ / _ \  | |\/| |/ _ \\\ \  / /| |/ _ \/ __|  |
|    | | | | | |  __/  | |  | | (_) |\ \/ / | |  __/\__ \  |
|    |_| |_| |_|\___|  |_|  |_|\___/  \__/  |_|\___||___/  |
|                                                          |
+----------------------------------------------------------+'''

    def start(self):
        """
        Начало работы приложения, устанавливает соединение с базой данных и запускает главное меню.
        """
        self.db_manager.connect()
        self.run_main_menu()

    def run_main_menu(self):
        """
        Запуск главного меню, которое отображает пользователю опции и обрабатывает их выбор.
        """
        while True:
            self.display_menu()
            choice = input(self.localization_manager.get_localized_text('choose_option'))
            self.result = self.display_results(self.db_manager.get_random_movies())
            self.process_choice(choice)

    @staticmethod
    def get_chunks(lst, chunk_size):
        """
        Разделение списка на отрезки.

        Параметры:
        ----------
        - lst: list
            Список для разделения.
        - chunk_size: int
            Размер отрезка.

        Возвращает:
        ----------
        - generator
            Генератор отрезков.
        """
        for i in range(0, len(lst), chunk_size):
            yield lst[i:i + chunk_size]

    def display_menu(self):
        """
        Отображение главного меню с различными опциями, включая смену языка и текущее состояние пользователя.
        """
        menu_items = [self.localization_manager.get_localized_text('change_language'),
                      self.localization_manager.get_localized_text('display_popular_queries')]

        if self.auth_manager.user_id != 0:
            menu_items.extend([
                '{}'.format(self.auth_manager.username),
                self.localization_manager.get_localized_text('logout'),
                self.localization_manager.get_localized_text('exit'),
            ])
        else:
            menu_items.extend([
                self.localization_manager.get_localized_text('register'),
                self.localization_manager.get_localized_text('login'),
                self.localization_manager.get_localized_text('exit'),
            ])

        menu_items.extend([
            self.localization_manager.get_localized_text('search_keyword'),
            self.localization_manager.get_localized_text('search_genre'),
            self.localization_manager.get_localized_text('search_year'),
            self.localization_manager.get_localized_text('search_actor'),
            self.localization_manager.get_localized_text('search_multiple_criteria'),
        ])

        result_display = []
        for idx, item in enumerate(menu_items, start=1):
            item_string = f'|[{idx}]{item}|'
            item_string = f'+{"-" * (len(item_string) - 2)}+\n{item_string}\n+{"-" * (len(item_string) - 2)}+'
            result_display.append(item_string.split('\n'))

        print(self.header)
        chunk_size = 5
        for chunk in self.get_chunks(result_display, chunk_size):
            chunk = list(zip(*chunk))
            for string in chunk:
                print(' '.join(string))

        print(self.result)

    def user_display(self):
        """
        Отображение информации о текущем пользователе, включая его идентификатор и имя.
        """
        menu_items = [self.localization_manager.get_localized_text('user_id').format(self.auth_manager.user_id),
                      self.localization_manager.get_localized_text('username').format(self.auth_manager.username)]
        max_len = 0
        for item in menu_items:
            max_len = len(item) if len(item) > max_len else max_len
        result_display = []
        sub_string = f'+{"-" * max_len}+'
        result_display.append(sub_string)
        for item in menu_items:
            item_string = '|{:<{width}}|'.format(item, width=max_len)
            result_display.append(item_string)
        result_display.append(sub_string)
        self.result = '\n'.join(result_display)

    def app_exit(self):
        """
        Выход из приложения, отключение от базы данных и очистка данных.
        """
        print(self.localization_manager.get_localized_text('app_exit_message'))
        if self.query_logger:
            del self.query_logger
        self.db_manager.disconnect()
        exit()

    def process_choice(self, choice):
        """
        Обработка выбора пользователя из главного меню: вызов соответствующей функции в зависимости от выбора.

        Параметры:
        ----------
        - choice: str
            Выбор пользователя.
        """
        if self.auth_manager.user_id != 0:
            choice3 = self.user_display
            choice4 = self.logout_user
        else:
            choice3 = self.register_user
            choice4 = self.login_user

        choice_item = [
            self.change_language,
            self.display_popular_search_queries,
            choice3,
            choice4,
            self.app_exit,
            self.search_movies_by_keyword,
            self.search_movies_by_genre,
            self.search_movies_by_year,
            self.search_movies_by_actor,
            self.search_movies_by_multiple_criteria
        ]

        if choice.isdigit() and 0 < int(choice) < len(choice_item) + 1:
            choice_item[int(choice) - 1]()
        else:
            self.result = self.localization_manager.get_localized_text('invalid_option')

    def search_movies_by_keyword(self):
        """
        Поиск фильмов по ключевым словам.
        """
        keywords = input(self.localization_manager.get_localized_text('enter_keyword'))
        self.query_logger.log_keyword_search(self.auth_manager.user_id, keywords)
        keywords = keywords.split()
        self.result = self.display_results(self.db_manager.search_movies(keywords=keywords))

    def search_movies_by_genre(self):
        """
        Поиск фильмов по жанру.
        """
        print('\n'.join(self.db_manager.fetch_column('category', 'name')))
        genre = input(self.localization_manager.get_localized_text('enter_genre'))
        self.query_logger.log_genre_search(self.auth_manager.user_id, genre)
        self.result = self.display_results(self.db_manager.search_movies(genre=genre))

    def search_movies_by_year(self):
        """
        Поиск фильмов по году выпуска.
        """
        year = input(self.localization_manager.get_localized_text('enter_year'))
        self.query_logger.log_year_search(self.auth_manager.user_id, year)
        self.result = self.display_results(self.db_manager.search_movies(start_year=year, end_year=year))

    def search_movies_by_actor(self):
        """
        Поиск фильмов по актерам.
        """
        actor = input(self.localization_manager.get_localized_text('enter_actor'))
        self.query_logger.log_actor_search(self.auth_manager.user_id, actor)
        self.result = self.display_results(self.db_manager.search_movies(actor_name=actor))

    def search_movies_by_multiple_criteria(self):
        """
        Поиск фильмов по нескольким критериям: ключевым словам, жанру, году выпуска, актерам.
        """
        keywords = input(self.localization_manager.get_localized_text('enter_keyword_optional'))
        print('\n'.join(self.db_manager.fetch_column('category', 'name')))
        genre = input(self.localization_manager.get_localized_text('enter_genre_optional'))
        start_year = input(self.localization_manager.get_localized_text('enter_start_year_optional'))
        end_year = input(self.localization_manager.get_localized_text('enter_end_year_optional'))
        actor = input(self.localization_manager.get_localized_text('enter_actor_optional'))
        print('\n'.join(['title', 'genre', 'release_year', 'actors']))
        sort_by = input(self.localization_manager.get_localized_text('sort_by')).lower()
        sort_order = input(self.localization_manager.get_localized_text('sort_order'))
        self.query_logger.log_multiple_criteria_search(self.auth_manager.user_id, keywords, genre,
                                                       start_year, end_year, actor)
        keywords = keywords.split()

        self.result = self.display_results(self.db_manager.search_movies(
            keywords=keywords or None,
            genre=genre or None,
            start_year=start_year or None,
            end_year=end_year or None,
            actor_name=actor or None,
            sort_by=sort_by or None,
            sort_order=sort_order if sort_order in ["ASC", "DESC"] else "ASC"
        ))

    def display_popular_search_queries(self):
        """
        Отображение популярных поисковых запросов, сохраненных в логах.
        """
        popular_queries = self.query_logger.get_popular_search_queries()
        popular_queries_list = [self.localization_manager.get_localized_text('popular_search_queries')]
        params_dict = {
            'keywords': self.localization_manager.get_localized_text('keywords'),
            'genre': self.localization_manager.get_localized_text('genre'),
            'year': self.localization_manager.get_localized_text('release_year'),
            'actor': self.localization_manager.get_localized_text('actors'),
            'end_year': self.localization_manager.get_localized_text('end_year'),
            'start_year': self.localization_manager.get_localized_text('start_year')
        }
        for idx, query in enumerate(popular_queries, start=1):
            search_type = query[0]
            search_params = json.loads(query[1])

            # Форматирование строки параметров запроса
            formatted_params = ', '.join(
                f"{params_dict[key]}: {value}" for key, value in search_params.items() if value)

            popular_queries_list.append(
                self.localization_manager.get_localized_text('query_details').format(idx, search_type,
                                                                                     formatted_params))
        self.result = '\n'.join(popular_queries_list)

    def register_user(self):
        """
        Регистрация нового пользователя в системе.
        """
        print(self.localization_manager.get_localized_text('register_prompt'))
        username = input(self.localization_manager.get_localized_text('enter_username'))
        password = input(self.localization_manager.get_localized_text('enter_password'))
        self.auth_manager.register_user(username, password)
        self.result = self.localization_manager.get_localized_text('registration_successful') \
            if self.auth_manager.user_id != 0 \
            else self.localization_manager.get_localized_text('registration_cancelled')

    def login_user(self):
        """
        Вход пользователя в систему.
        """
        print(self.localization_manager.get_localized_text('login_prompt'))
        username = input(self.localization_manager.get_localized_text('enter_username'))
        password = input(self.localization_manager.get_localized_text('enter_password'))
        user_id = self.auth_manager.login_user(username, password)
        if user_id:
            self.result = self.localization_manager.get_localized_text('login_successful').format(username=username)
        else:
            self.result = self.localization_manager.get_localized_text('login_failed')

    def logout_user(self):
        """
        Выход пользователя из системы.
        """
        self.auth_manager.logout_user()
        self.result = self.localization_manager.get_localized_text('logout_successful')

    def change_language(self):
        """
        Изменение языка интерфейса приложения.
        """
        new_language = self.select_language()
        if new_language != self.localization_manager.current_language_code:
            self.localization_manager.change_language(new_language)
            self.result = self.localization_manager.get_localized_text('language_changed').format(language=new_language)

    def select_language(self):
        """
        Выбор нового языка интерфейса из доступных опций.

        Возвращает:
        ----------
        - str
            Код нового языка.
        """
        select_languages = self.db_manager.fetch_column('language_pack', 'language_name')
        select_languages = [self.localization_manager.get_localized_text(x.lower()) for x in select_languages]
        select_code = self.db_manager.fetch_column('language_pack', 'language_code')
        for idx, item in enumerate(select_languages, start=1):
            print(f'{idx}. {item}')
        choice = input(self.localization_manager.get_localized_text('choose_language'))
        if choice.isdigit() and 0 < int(choice) < len(select_code) + 1:
            return select_code[int(choice) - 1]
        else:
            self.result = self.localization_manager.get_localized_text('invalid_option')
            return self.localization_manager.current_language_code

    def display_results(self, results=None):
        """
        Отображение результатов поиска фильмов в форматированном виде.

        Параметры:
        ----------
        - results: list
            Список фильмов для отображения (по умолчанию None).

        Возвращает:
        ----------
        - str
            Отформатированная строка с результатами поиска фильмов.
        """
        result_list = []
        width = len(self.localization_manager.get_localized_text('release_year'))

        # Create header
        result_list.append("+{:-<32}+{:-<22}+{:-<{width}}+{:-<40}".format("", "", "", "", width=width + 2))
        result_list.append("| {:<30} | {:<20} | {:<{width}} | {:<40}".format(
            self.localization_manager.get_localized_text('title'),
            self.localization_manager.get_localized_text('genre'),
            self.localization_manager.get_localized_text('release_year'),
            self.localization_manager.get_localized_text('actors'),
            width=width
        ))
        result_list.append("+{:-<32}+{:-<22}+{:-<{width}}+{:-<40}".format("", "", "", "", width=width + 2))

        if results:
            for film in results:
                title = film.get('title') or ''
                genre = film.get('genre') or ''
                release_year = film.get('release_year') or ''
                actors = film.get('actors') or ''

                result_list.append("| {:<30} | {:<20} | {:<{width}} | {:<40}".format(
                    title, genre, release_year, actors, width=width
                ))

            result_list.append("+{:-<32}+{:-<22}+{:-<{width}}+{:-<40}".format("", "", "", "", width=width + 2))
            return '\n'.join(result_list)
        else:
            return self.localization_manager.get_localized_text('no_results_found')

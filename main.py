"""
main.py
-----------------------
Главный скрипт для запуска приложения по поиску фильмов.

Этот скрипт создает экземпляр класса FilmSearchApp, который инициализирует приложение и запускает его.

Использование:
    Запустите этот скрипт для запуска консольного приложения по поиску фильмов.
"""
from config import DATABASE_CONFIG
from film_search_app import FilmSearchApp


def main():
    """
    Инициализирует и запускает приложение FilmSearchApp.

    Создает экземпляр класса FilmSearchApp, используя конфигурацию базы данных
    DATABASE_CONFIG из модуля config. Затем вызывает метод start() для запуска приложения.
    """
    app = FilmSearchApp(DATABASE_CONFIG)
    app.start()


if __name__ == "__main__":
    main()

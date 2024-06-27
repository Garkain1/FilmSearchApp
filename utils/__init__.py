"""
utils/__init__.py

Инициализация пакета утилит.

Импортируемые модули:
----------------------
load_localization_texts_from_file: Функция для загрузки текстов локализации из файла.

Примеры использования:
----------------------
from utils import load_localization_texts_from_file

localization_texts = load_localization_texts_from_file('language_pack.json')
# Использование localization_texts для доступа к текстам локализации в приложении.
"""
from .localization import load_localization_texts_from_file

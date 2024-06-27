-- Использовать базу данных project_220424_oskolkov;
use project_220424_oskolkov;

-- Вставка записи для белорусского языка в таблицу language_pack
INSERT INTO language_pack (language_code, language_name) VALUES
('be', 'Belarusian'); -- Вставляем запись для белорусского языка

-- Вставка локализованных текстов на белорусском языке в таблицу localized_text  (language_id = 6)
INSERT INTO localized_text (language_id, text_key, text_value) VALUES
(6, 'change_language', 'Змена мовы'),
(6, 'english', 'Англійская'),
(6, 'german', 'Нямецкая'),
(6, 'russian', 'Руская'),
(6, 'ukrainian', 'Украінская'),
(6, 'georgian', 'Грузінская'),
(6, 'belarusian', 'Беларуская'),
(6, 'search_keyword', 'Пошук па ключавым слове'),
(6, 'search_genre', 'Пошук па жанру'),
(6, 'search_year', 'Пошук па годзе'),
(6, 'search_actor', 'Пошук па акцёру'),
(6, 'search_multiple_criteria', 'Пошук па некалькіх крытэрывах'),
(6, 'display_popular_queries', 'Адлюстраваць папулярныя запыты'),
(6, 'logout', 'Выйсці'),
(6, 'register', 'Рэгістрацыя'),
(6, 'login', 'Уваход'),
(6, 'exit', 'Выйсці з прыкладання'),
(6, 'choose_option', 'Выберыце варыянт: '),
(6, 'invalid_option', 'Няправільны варыянт, калі ласка, паспрабуйце яшчэ раз.'),
(6, 'enter_keyword', 'Увядзіце ключавое слова: '),
(6, 'enter_genre', 'Увядзіце жанр: '),
(6, 'enter_year', 'Увядзіце год: '),
(6, 'enter_actor', 'Увядзіце імя акцёра: '),
(6, 'user_id', 'ID карыстальніка: {}'),
(6, 'username', 'Імя карыстальніка: {}'),
(6, 'app_exit_message', 'Завяршэнне прыкладання...'),
(6, 'enter_keyword_optional', 'Увядзіце ключавое слова (неабавязкова): '),
(6, 'enter_genre_optional', 'Увядзіце жанр (неабавязкова): '),
(6, 'enter_start_year_optional', 'Увядзіце пачатковы год (неабавязкова): '),
(6, 'enter_end_year_optional', 'Увядзіце канчатковы год (неабавязкова): '),
(6, 'enter_actor_optional', 'Увядзіце імя акцёра (неабавязкова): '),
(6, 'popular_search_queries', 'Папулярныя запыты: '),
(6, 'sort_by', 'Сартаваць па (неабавязкова): '),
(6, 'sort_order', 'Парадак сартавання (ASC/DESC, неабавязкова): '),
(6, 'search_logs', 'Працяг пошуку:'),
(6, 'search_query', 'Пошукавы запыт'),
(6, 'search_time', 'Час'),
(6, 'title', 'Назва'),
(6, 'release_year', 'Год выпуску'),
(6, 'genre', 'Жанр'),
(6, 'actors', 'Акцёры'),
(6, 'keywords', 'Ключавыя словы'),
(6, 'end_year', 'Канчатковы год'),
(6, 'start_year', 'Пачатковы год'),
(6, 'username_exists', 'Карыстальнік з імем {} ўжо існуе'),
(6, 'try_again_prompt', 'Калі ласка, увядзіце "назад", каб вярнуцца, або націсніце Enter, каб паспрабаваць яшчэ раз: '),
(6, 'back', 'назад'),
(6, 'query_details', '{}. Тып пошуку: {}, параметры: {}.'),
(6, 'no_results_found', 'Няма вынікаў'),
(6, 'enter_username', 'Увядзіце імя карыстальніка: '),
(6, 'enter_password', 'Увядзіце пароль: '),
(6, 'register_prompt', 'Рэгістрацыя:'),
(6, 'choose_language', 'Выберыце мову: '),
(6, 'language_changed', 'Мова зменена паспяхова.'),
(6, 'registration_successful', 'Рэгістрацыя паспяхова завершана.'),
(6, 'registration_cancelled', 'Рэгістрацыя адмяненая.'),
(6, 'logout_successful', 'Выхад паспяховы.'),
(6, 'login_prompt', 'Уваход:'),
(6, 'login_successful', 'Уваход паспяховы'),
(6, 'login_failed', 'Уваход не ўдалось. Калі ласка, праверце вашыя крэдыціці і паспрабуйце яшчэ раз.'); -- Вставляем локализованные тексты для белорусского языка

-- Дополнительные вставки записей для белорусского языка в таблицу localized_text для других языков
-- Английский
INSERT INTO localized_text (language_id, text_key, text_value) VALUES
(1, 'belarusian', 'Belarusian'); -- Вставляем белорусский язык на английском

-- Немецкий
INSERT INTO localized_text (language_id, text_key, text_value) VALUES
(2, 'belarusian', 'Belarussisch'); -- Вставляем белорусский язык на немецком

-- Русский
INSERT INTO localized_text (language_id, text_key, text_value) VALUES
(3, 'belarusian', 'Белорусский'); -- Вставляем белорусский язык на русском

-- Украинский
INSERT INTO localized_text (language_id, text_key, text_value) VALUES
(4, 'belarusian', 'Білоруська'); -- Вставляем белорусский язык на украинском

-- Грузинский
INSERT INTO localized_text (language_id, text_key, text_value) VALUES
(5, 'belarusian', 'ბელორუსი'); -- Вставляем белорусский язык на грузинском
-- Код на SQL для создания базы данных, содержащей информацию о языковых пакетах и локализованных текстах для различных языков.

-- Использовать базу данных project_220424_oskolkov
use project_220424_oskolkov;

-- Удалить таблицу localized_text, если она существует
drop table if exists localized_text;

-- Удалить таблицу language_pack, если она существует
drop table if exists language_pack;

-- Создать таблицу language_pack для хранения информации о языках
CREATE TABLE language_pack (
    language_id INT AUTO_INCREMENT PRIMARY KEY, -- Уникальный идентификатор языка
    language_code VARCHAR(10) NOT NULL, -- Код языка
    language_name VARCHAR(100) NOT NULL -- Название языка
);

-- Создать таблицу localized_text для хранения локализованных текстов
CREATE TABLE localized_text (
    language_id INT, -- Идентификатор языка (внешний ключ)
    text_key VARCHAR(255) NOT NULL, -- Ключ текста
    text_value TEXT NOT NULL, -- Значение текста
    FOREIGN KEY (language_id) REFERENCES language_pack(language_id) -- Связь с таблицей language_pack
);

-- Вставить данные для языков в таблицу language_pack
INSERT INTO language_pack (language_code, language_name) VALUES
('en', 'English'),
('de', 'German'),
('ru', 'Russian'),
('uk', 'Ukrainian'),
('ka', 'Georgian');

-- Вставить локализованные тексты для английского языка (language_id = 1)
INSERT INTO localized_text (language_id, text_key, text_value) VALUES
(1, 'change_language', 'Change language'),
(1, 'english', 'English'),
(1, 'german', 'German'),
(1, 'russian', 'Russian'),
(1, 'ukrainian', 'Ukrainian'),
(1, 'georgian', 'Georgian'),
(1, 'search_keyword', 'Search by keyword'),
(1, 'search_genre', 'Search by genre'),
(1, 'search_year', 'Search by year'),
(1, 'search_actor', 'Search by actor'),
(1, 'search_multiple_criteria', 'Search by multiple criteria'),
(1, 'display_popular_queries', 'Display popular queries'),
(1, 'logout', 'Logout'),
(1, 'register', 'Register'),
(1, 'login', 'Login'),
(1, 'exit', 'Exit'),
(1, 'choose_option', 'Choose an option: '),
(1, 'invalid_option', 'Invalid option, please try again.'),
(1, 'enter_keyword', 'Enter keyword: '),
(1, 'enter_genre', 'Enter genre: '),
(1, 'enter_year', 'Enter year: '),
(1, 'enter_actor', 'Enter actor name: '),
(1, 'user_id', 'User ID: {}'),
(1, 'username', 'Username: {}'),
(1, 'app_exit_message', 'Exiting the application...'),
(1, 'enter_keyword_optional', 'Enter keyword (optional): '),
(1, 'enter_genre_optional', 'Enter genre (optional): '),
(1, 'enter_start_year_optional', 'Enter start year (optional): '),
(1, 'enter_end_year_optional', 'Enter end year (optional): '),
(1, 'enter_actor_optional', 'Enter actor name (optional): '),
(1, 'popular_search_queries', 'Popular search queries:'),
(1, 'sort_by', 'Sort by (optional): '),
(1, 'sort_order', 'Sort order (ASC/DESC, optional): '),
(1, 'search_logs', 'Search Logs:'),
(1, 'search_query', 'Search Query'),
(1, 'search_time', 'Time'),
(1, 'title', 'Title'),
(1, 'release_year', 'Release Year'),
(1, 'genre', 'Genre'),
(1, 'actors', 'Actors'),
(1, 'keywords', 'Keywords'),
(1, 'end_year', 'End Year'),
(1, 'start_year', 'Start Year'),
(1, 'username_exists', 'A user with the name {} already exists'),
(1, 'try_again_prompt', 'Type "back" to return or press Enter to try again: '),
(1, 'back', 'back'),
(1, 'query_details', '{}. Search type: {}, parameters: {}.'),
(1, 'no_results_found', 'No results found'),
(1, 'enter_username', 'Enter username: '),
(1, 'enter_password', 'Enter password: '),
(1, 'register_prompt', 'Register:'),
(1, 'choose_language', 'Choose language: '),
(1, 'language_changed', 'Language changed successfully.'),
(1, 'registration_successful', 'Registration successful.'),
(1, 'registration_cancelled', 'Registration cancelled.'),
(1, 'logout_successful', 'Logout successful.'),
(1, 'login_prompt', 'Login:'),
(1, 'login_successful', 'Login successful'),
(1, 'login_failed', 'Login failed. Please check your credentials and try again.');

-- Вставить локализованные тексты для немецкого языка (language_id = 2)
INSERT INTO localized_text (language_id, text_key, text_value) VALUES
(2, 'change_language', 'Sprache ändern'),
(2, 'english', 'Englisch'),
(2, 'german', 'Deutsch'),
(2, 'russian', 'Russisch'),
(2, 'ukrainian', 'Ukrainisch'),
(2, 'georgian', 'Georgisch'),
(2, 'search_keyword', 'Nach Stichwort suchen'),
(2, 'search_genre', 'Nach Genre suchen'),
(2, 'search_year', 'Nach Jahr suchen'),
(2, 'search_actor', 'Nach Schauspieler suchen'),
(2, 'search_multiple_criteria', 'Suche nach mehreren Kriterien'),
(2, 'display_popular_queries', 'Beliebte Suchanfragen anzeigen'),
(2, 'logout', 'Abmelden'),
(2, 'register', 'Registrieren'),
(2, 'login', 'Anmelden'),
(2, 'exit', 'Ausgang'),
(2, 'choose_option', 'Wählen Sie eine Option: '),
(2, 'invalid_option', 'Ungültige Option, bitte versuchen Sie es erneut.'),
(2, 'enter_keyword', 'Stichwort eingeben: '),
(2, 'enter_genre', 'Genre eingeben: '),
(2, 'enter_year', 'Jahr eingeben: '),
(2, 'enter_actor', 'Schauspielername eingeben: '),
(2, 'user_id', 'Benutzer ID: {}'),
(2, 'username', 'Benutzername: {}'),
(2, 'app_exit_message', 'Anwendung wird beendet...'),
(2, 'enter_keyword_optional', 'Stichwort eingeben (optional): '),
(2, 'enter_genre_optional', 'Genre eingeben (optional): '),
(2, 'enter_start_year_optional', 'Startjahr eingeben (optional): '),
(2, 'enter_end_year_optional', 'Endjahr eingeben (optional): '),
(2, 'enter_actor_optional', 'Schauspielername eingeben (optional): '),
(2, 'popular_search_queries', 'Beliebte Suchanfragen: '),
(2, 'sort_by', 'Sortieren nach (optional): '),
(2, 'sort_order', 'Sortierreihenfolge (ASC/DESC, optional): '),
(2, 'search_logs', 'Suchprotokolle:'),
(2, 'search_query', 'Suchanfrage'),
(2, 'search_time', 'Zeit'),
(2, 'title', 'Titel'),
(2, 'release_year', 'Erscheinungsjahr'),
(2, 'genre', 'Genre'),
(2, 'actors', 'Schauspieler'),
(2, 'keywords', 'Schlüsselwörter'),
(2, 'end_year', 'Endjahr'),
(2, 'start_year', 'Startjahr'),
(2, 'username_exists', 'Ein Benutzer mit dem Namen {} existiert bereits'),
(2, 'try_again_prompt', 'Geben Sie "zurück" ein, um zurückzukehren oder drücken Sie die Eingabetaste, um es erneut zu versuchen: '),
(2, 'back', 'zurück'),
(2, 'query_details', '{}. Suchtyp: {}, Parameter: {}.'),
(2, 'no_results_found', 'Keine Ergebnisse gefunden'),
(2, 'enter_username', 'Benutzernamen eingeben: '),
(2, 'enter_password', 'Passwort eingeben: '),
(2, 'register_prompt', 'Registrieren:'),
(2, 'choose_language', 'Wählen Sie die Sprache: '),
(2, 'language_changed', 'Sprache erfolgreich geändert.'),
(2, 'registration_successful', 'Registrierung erfolgreich.'),
(2, 'registration_cancelled', 'Registrierung abgebrochen.'),
(2, 'logout_successful', 'Abmeldung erfolgreich.'),
(2, 'login_prompt', 'Anmeldung:'),
(2, 'login_successful', 'Anmeldung erfolgreich'),
(2, 'login_failed', 'Anmeldung fehlgeschlagen. Bitte überprüfen Sie Ihre Anmeldeinformationen und versuchen Sie es erneut.');

-- Вставить локализованные тексты для русского языка (language_id = 3)
INSERT INTO localized_text (language_id, text_key, text_value) VALUES
(3, 'change_language', 'Изменить язык'),
(3, 'english', 'Английский'),
(3, 'german', 'Немецкий'),
(3, 'russian', 'Русский'),
(3, 'ukrainian', 'Украинский'),
(3, 'georgian', 'Грузинский'),
(3, 'search_keyword', 'Поиск по ключевому слову'),
(3, 'search_genre', 'Поиск по жанру'),
(3, 'search_year', 'Поиск по году'),
(3, 'search_actor', 'Поиск по актеру'),
(3, 'search_multiple_criteria', 'Поиск по нескольким критериям'),
(3, 'display_popular_queries', 'Отобразить популярные запросы'),
(3, 'logout', 'Выход'),
(3, 'register', 'Регистрация'),
(3, 'login', 'Вход'),
(3, 'exit', 'Закрыть приложение'),
(3, 'choose_option', 'Выберите опцию: '),
(3, 'invalid_option', 'Неверная опция, пожалуйста, попробуйте еще раз.'),
(3, 'enter_keyword', 'Введите ключевое слово: '),
(3, 'enter_genre', 'Введите жанр: '),
(3, 'enter_year', 'Введите год: '),
(3, 'enter_actor', 'Введите имя актера: '),
(3, 'user_id', 'ID пользователя: {}'),
(3, 'username', 'Имя пользователя: {}'),
(3, 'app_exit_message', 'Выход из приложения...'),
(3, 'enter_keyword_optional', 'Введите ключевое слово (опционально): '),
(3, 'enter_genre_optional', 'Введите жанр (опционально): '),
(3, 'enter_start_year_optional', 'Введите начальный год (опционально): '),
(3, 'enter_end_year_optional', 'Введите конечный год (опционально): '),
(3, 'enter_actor_optional', 'Введите имя актера (опционально): '),
(3, 'popular_search_queries', 'Популярные запросы:'),
(3, 'sort_by', 'Сортировать по (опционально): '),
(3, 'sort_order', 'Порядок сортировки (ASC/DESC, опционально): '),
(3, 'search_logs', 'Журнал поиска:'),
(3, 'search_query', 'Запрос поиска'),
(3, 'search_time', 'Время'),
(3, 'title', 'Название'),
(3, 'release_year', 'Год выпуска'),
(3, 'genre', 'Жанр'),
(3, 'actors', 'Актеры'),
(3, 'keywords', 'Ключевые слова'),
(3, 'end_year', 'Конечный год'),
(3, 'start_year', 'Начальный год'),
(3, 'username_exists', 'Пользователь с именем {} уже существует'),
(3, 'try_again_prompt', 'Введите "назад", чтобы вернуться, или нажмите Enter, чтобы попробовать снова: '),
(3, 'back', 'назад'),
(3, 'query_details', '{}. Тип поиска: {}, параметры: {}.'),
(3, 'no_results_found', 'Результаты не найдены'),
(3, 'enter_username', 'Введите имя пользователя: '),
(3, 'enter_password', 'Введите пароль: '),
(3, 'register_prompt', 'Регистрация:'),
(3, 'choose_language', 'Выберите язык: '),
(3, 'language_changed', 'Язык успешно изменен.'),
(3, 'registration_successful', 'Регистрация успешна.'),
(3, 'registration_cancelled', 'Регистрация отменена.'),
(3, 'logout_successful', 'Выход выполнен успешно.'),
(3, 'login_prompt', 'Вход:'),
(3, 'login_successful', 'Вход успешно выполнен'),
(3, 'login_failed', 'Ошибка входа. Пожалуйста, проверьте ваши учетные данные и попробуйте снова.');

-- Вставить локализованные тексты для украинского языка (language_id = 4)
INSERT INTO localized_text (language_id, text_key, text_value) VALUES
(4, 'change_language', 'Змінити мову'),
(4, 'english', 'Англійська'),
(4, 'german', 'Німецька'),
(4, 'russian', 'Російська'),
(4, 'ukrainian', 'Українська'),
(4, 'georgian', 'Грузинська'),
(4, 'search_keyword', 'Пошук за ключовим словом'),
(4, 'search_genre', 'Пошук за жанром'),
(4, 'search_year', 'Пошук за роком'),
(4, 'search_actor', 'Пошук за актором'),
(4, 'search_multiple_criteria', 'Пошук за кількома критеріями'),
(4, 'display_popular_queries', 'Показати популярні запити'),
(4, 'logout', 'Вийти'),
(4, 'register', 'Зареєструватися'),
(4, 'login', 'Увійти'),
(4, 'exit', 'Вийти з програми'),
(4, 'choose_option', 'Виберіть опцію: '),
(4, 'invalid_option', 'Невірна опція, спробуйте ще раз.'),
(4, 'enter_keyword', 'Введіть ключове слово: '),
(4, 'enter_genre', 'Введіть жанр: '),
(4, 'enter_year', 'Введіть рік: '),
(4, 'enter_actor', 'Введіть ім\'я актора: '),
(4, 'user_id', 'Ідентифікатор користувача: {}'),
(4, 'username', 'Ім\'я користувача: {}'),
(4, 'app_exit_message', 'Вихід з програми...'),
(4, 'enter_keyword_optional', 'Введіть ключове слово (необов\'язково): '),
(4, 'enter_genre_optional', 'Введіть жанр (необов\'язково): '),
(4, 'enter_start_year_optional', 'Введіть початковий рік (необов\'язково): '),
(4, 'enter_end_year_optional', 'Введіть кінцевий рік (необов\'язково): '),
(4, 'enter_actor_optional', 'Введіть ім\'я актора (необов\'язково): '),
(4, 'popular_search_queries', 'Популярні пошукові запити: '),
(4, 'sort_by', 'Сортувати за (необов\'язково): '),
(4, 'sort_order', 'Порядок сортування (ASC/DESC, необов\'язково): '),
(4, 'search_logs', 'Журнал пошуку:'),
(4, 'search_query', 'Пошуковий запит'),
(4, 'search_time', 'Час'),
(4, 'title', 'Назва'),
(4, 'release_year', 'Рік випуску'),
(4, 'genre', 'Жанр'),
(4, 'actors', 'Актори'),
(4, 'keywords', 'Ключові слова'),
(4, 'end_year', 'Кінцевий рік'),
(4, 'start_year', 'Початковий рік'),
(4, 'username_exists', 'Користувач з іменем {} вже існує'),
(4, 'try_again_prompt', 'Введіть "назад", щоб повернутися, або натисніть Enter, щоб спробувати знову: '),
(4, 'back', 'назад'),
(4, 'query_details', '{}. Тип пошуку: {}, параметри: {}.'),
(4, 'no_results_found', 'Результати не знайдені'),
(4, 'enter_username', 'Введіть ім\'я користувача: '),
(4, 'enter_password', 'Введіть пароль: '),
(4, 'register_prompt', 'Реєстрація:'),
(4, 'choose_language', 'Виберіть мову: '),
(4, 'language_changed', 'Мова успішно змінена.'),
(4, 'registration_successful', 'Реєстрація пройшла успішно.'),
(4, 'registration_cancelled', 'Реєстрацію скасовано.'),
(4, 'logout_successful', 'Вихід із системи успішний.'),
(4, 'login_prompt', 'Логін:'),
(4, 'login_successful', 'Вхід успішний'),
(4, 'login_failed', 'Невдалий вхід. Перевірте свої облікові дані та спробуйте ще раз.');

-- Вставить локализованные тексты для грузинского языка (language_id = 5)
INSERT INTO localized_text (language_id, text_key, text_value) VALUES
(5, 'change_language', 'ენის შეცვლა'),
(5, 'english', 'ინგლისური'),
(5, 'german', 'გერმანული'),
(5, 'russian', 'რუსული'),
(5, 'ukrainian', 'უკრაინული'),
(5, 'georgian', 'ქართული'),
(5, 'search_keyword', 'ძიება კითხვის მიხედვით'),
(5, 'search_genre', 'ძიება ჟანრის მიხედვით'),
(5, 'search_year', 'ძიება წელის მიხედვით'),
(5, 'search_actor', 'ძიება მსახიობის მიხედვით'),
(5, 'search_multiple_criteria', 'ძიება რამდენიმე კრიტერიუმით'),
(5, 'display_popular_queries', 'პოპულარული მოთხოვნების ჩვენება'),
(5, 'logout', 'გასვლა'),
(5, 'register', 'რეგისტრაცია'),
(5, 'login', 'შესვლა'),
(5, 'exit', 'გასვლა აპლიკაციიდან'),
(5, 'choose_option', 'აირჩიეთ ოფცია: '),
(5, 'invalid_option', 'არასწორი ოფცია, გთხოვთ სცადოთ თავიდან.'),
(5, 'enter_keyword', 'შეიყვანეთ კითხვის სიტყვა: '),
(5, 'enter_genre', 'შეიყვანეთ ჟანრი: '),
(5, 'enter_year', 'შეიყვანეთ წელი: '),
(5, 'enter_actor', 'შეიყვანეთ მსახიობის სახელი: '),
(5, 'user_id', 'მომხმარებელი ID: {}'),
(5, 'username', 'მომხმარებელის სახელი: {}'),
(5, 'app_exit_message', 'აპლიკაციიდან გამოსვლა...'),
(5, 'enter_keyword_optional', 'შეიყვანეთ კითხვის სიტყვა (არასავალდებულო): '),
(5, 'enter_genre_optional', 'შეიყვანეთ ჟანრი (არასავალდებულო): '),
(5, 'enter_start_year_optional', 'შეიყვანეთ დაწყებული წელი (არასავალდებულო): '),
(5, 'enter_end_year_optional', 'შეიყვანეთ ბოლო წელი (არასავალდებულო): '),
(5, 'enter_actor_optional', 'შეიყვანეთ მსახიობის სახელი (არასავალდებულო): '),
(5, 'popular_search_queries', 'პოპულარული ძებნის მოთხოვნები: '),
(5, 'sort_by', 'სორტირება მიხედვით (არასავალდებულო): '),
(5, 'sort_order', 'სორტირების მიმდევრობა (ASC/DESC, არასავალდებულო): '),
(5, 'search_logs', 'ძებნის ჟურნალი:'),
(5, 'search_query', 'ძებნის მოთხოვნა'),
(5, 'search_time', 'დრო'),
(5, 'title', 'სათაური'),
(5, 'release_year', 'გამოსაშვები წელი'),
(5, 'genre', 'ჟანრი'),
(5, 'actors', 'მსახიობები'),
(5, 'keywords', 'საკეტეგორო სიტყვები'),
(5, 'end_year', 'ბოლო წელი'),
(5, 'start_year', 'დაწყების წელი'),
(5, 'username_exists', 'მომხმარებელი {} უკვე არსებობს'),
(5, 'try_again_prompt', 'ჩაწერეთ "უკან", რათა დაბრუნდეს ან დააჭირეთ Enter, რათა სცადოთ თავიდან: '),
(5, 'back', 'უკან'),
(5, 'query_details', '{}. ძიების ტიპი: {}, პარამეტრები: {}.'),
(5, 'no_results_found', 'შედეგები არ მოიძებნა'),
(5, 'enter_username', 'შეიყვანეთ მომხმარებელის სახელი: '),
(5, 'enter_password', 'შეიყვანეთ პაროლი: '),
(5, 'register_prompt', 'რეგისტრაცია:'),
(5, 'choose_language', 'აირჩიეთ ენა: '),
(5, 'language_changed', 'ენა შეიცვალა წარმატებით.'),
(5, 'registration_successful', 'რეგისტრაცია წარმატებით დასრულდა.'),
(5, 'registration_cancelled', 'რეგისტრაცია გაუქმდა.'),
(5, 'logout_successful', 'გამოსვლა წარმატებით.'),
(5, 'login_prompt', 'შესვლა:'),
(5, 'login_successful', 'შესვლა წარმატებით'),
(5, 'login_failed', 'შესვლა ვერ მოხერხდა. გთხოვთ, შეამოწმეთ თქვენი მონაცემები და სცადოთ თავიდან.');
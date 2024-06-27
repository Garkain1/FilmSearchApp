-- Удаление таблицы user_queries, если она существует
DROP TABLE IF EXISTS user_queries;

-- Создание таблицы для хранения запросов пользователей
CREATE TABLE user_queries (
    query_id INT AUTO_INCREMENT PRIMARY KEY, -- Уникальный идентификатор запроса
    user_id INT NOT NULL, -- Идентификатор пользователя, выполнившего запрос
    search_type VARCHAR(50) NOT NULL, -- Тип поискового запроса (например, по ключевому слову, по жанру и т.д.)
    search_params JSON NOT NULL, -- Параметры поискового запроса в формате JSON
    query_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Время выполнения запроса
);

-- Комментарии к столбцам:
-- - query_id: Уникальный номер каждого запроса
-- - user_id: Идентификатор пользователя, выполнившего запрос
-- - search_type: Тип поискового запроса, например, "keyword", "genre", "multiple criteria"
-- - search_params: Параметры поискового запроса, хранятся в формате JSON для гибкости структуры
-- - query_time: Время выполнения запроса, записывается автоматически при вставке данных

-- Создание индекса для ускорения поиска по user_id (если требуется)
-- CREATE INDEX idx_user_id ON user_queries (user_id);

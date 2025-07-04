## 📌 Содержание
1. [Требования](#-требования)
2. [Структура проекта](#-структура-проекта)
3. [Настройка окружения](#-настройка-окружения)
4. [Запуск проекта](#-запуск-проекта)
5. [Работа с медиа](#-работа-с-медиа)

---

## 📋 Требования
- Python 3.9+
- PostgreSQL 12+
- Аккаунт Yandex для почтового сервиса

---

## 📂 Структура проекта

```
.
├── auth/                        # Модуль аутентификации
│   └── __pycache__/
│
├── mail/                        # Модуль работы с почтой
│   └── __pycache__/
│
├── media/                       # Модуль работы с медиа
│   └── __pycache__/
│
├── migrations/                  # Миграции базы данных
│   ├── versions/                # Файлы миграций
│   │   └── __pycache__/
│   └── __pycache__/
│
├── static/                      # Статические файлы
│   ├── audio/                   # Аудио файлы
│   ├── image/                   # Изображения
│   └── video/                   # Видео файлы
│
└── __pycache__/                 # Кэш Python
```

---

## ⚙️ Настройка окружения

Создайте `.env` файл в корне проекта:

```ini
# Аутентификация
JWT_SECRET_KEY="ваш_секретный_ключ_минимум_32_символа"
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# Почта (Yandex)
SMTP_HOST="smtp.yandex.ru"
SMTP_PORT=465
SMTP_USER="ваш@yandex.ru"
SMTP_PASSWORD="пароль_приложения"
EMAILS_FROM_EMAIL="ваш@yandex.ru"

# База данных
POSTGRES_SERVER="ваш.postgres.server"
POSTGRES_USER="ваш_user"
POSTGRES_PASSWORD="ваш_пароль"
POSTGRES_DB="ваша_бд"
DATABASE_URL="postgresql://user:pass@host:port/dbname"
```

---

## 🚀 Запуск проекта

1. **Установка зависимостей**:
   ```bash
   pip install -r req.txt
   ```

2. **Настройка базы данных**:
   ```bash
   alembic upgrade head
   ```

3. **Запуск сервера**:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

Сервер будет доступен по адресу:  
[http://localhost:8000](http://localhost:8000)

Документация API:  
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🖼 Работа с медиа

Проект поддерживает хранение медиафайлов в следующих директориях:
- `static/audio/` - для аудиофайлов
- `static/image/` - для изображений
- `static/video/` - для видеофайлов
---

## ⚠️ Важные замечания

1. Для работы почты используйте [пароль приложения](https://yandex.ru/support/id/authorization/app-passwords.html) Яндекса
2. Директории `__pycache__` создаются автоматически и не требуют ручного вмешательства
3. Для продакшн-окружения:
   - Используйте HTTPS
   - Отключите debug-режим
   - Настройте правильные права на медиафайлы

---

Для Docker-развертывания добавьте соответствующие инструкции в отдельный раздел.

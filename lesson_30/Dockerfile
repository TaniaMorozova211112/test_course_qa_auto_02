# Базовий образ Python 3.11 slim
FROM python:3.11-slim

# Встановлюємо клієнт PostgreSQL (щоб був pg_isready) та очищуємо кеш
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Робоча директорія в контейнері
WORKDIR /app

# Копіюємо файл з залежностями
COPY requirements.txt .

# Встановлюємо Python-залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код у контейнер
COPY . .

# Дозволяємо виконувати скрипт очікування PostgreSQL
RUN chmod +x wait-for-postgres.sh

# Команда запуску: спочатку чекаємо PostgreSQL, потім запускаємо тести з Allure
CMD ["./wait-for-postgres.sh", "pytest", "-v", "--alluredir=allure-results"]

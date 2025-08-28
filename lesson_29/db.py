# Модуль для підключення до PostgreSQL

import psycopg2

def get_connection():
    return psycopg2.connect(
        host="postgres-db",  # <- змінили з "db" на ім'я контейнера Postgres
        database="testdb",
        user="postgres",
        password="postgres"
    )

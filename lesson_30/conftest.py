import pytest
import psycopg2

@pytest.fixture(scope="module")
def db_connection():
    conn = psycopg2.connect(
        dbname="testdb",
        user="postgres",
        password="postgres",
        host="127.0.0.1",  # замість "postgres-db"
        port="5433"         # порт, на якому ти запустила контейнер
    )
    yield conn
    conn.close()

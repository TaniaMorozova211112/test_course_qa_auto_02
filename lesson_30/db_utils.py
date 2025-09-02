# Утиліти для роботи з БД

def create_table(conn):
    """
    Створює таблицю users, якщо її ще немає.
    """
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                age INT
            );
        """)
        conn.commit()

def insert_user(conn, name, age):
    """
    Вставка нового користувача. Повертає його id.
    """
    with conn.cursor() as cur:
        cur.execute("INSERT INTO users (name, age) VALUES (%s, %s) RETURNING id;", (name, age))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id

def update_user(conn, user_id, name, age):
    """
    Оновлення даних користувача за id.
    """
    with conn.cursor() as cur:
        cur.execute("UPDATE users SET name=%s, age=%s WHERE id=%s;", (name, age, user_id))
        conn.commit()

def delete_user(conn, user_id):
    """
    Видалення користувача за id.
    """
    with conn.cursor() as cur:
        cur.execute("DELETE FROM users WHERE id=%s;", (user_id,))
        conn.commit()

def get_users(conn):
    """
    Повертає список усіх користувачів.
    """
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users;")
        return cur.fetchall()

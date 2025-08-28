# Основний код для роботи з базою

from db import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            age INT
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_user(name, age):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s) RETURNING id;", (name, age))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id

def update_user(user_id, name, age):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name=%s, age=%s WHERE id=%s;", (name, age, user_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s;", (user_id,))
    conn.commit()
    cur.close()
    conn.close()

def get_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

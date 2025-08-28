# Тести на вставку, оновлення, видалення, вибірку

import pytest
from app import create_table, insert_user, update_user, delete_user, get_users


def test_crud_operations():
    create_table()  # всередині викликає get_connection()

    # Вставка
    user_id = insert_user("Alice", 25)
    users = get_users()
    assert any(u[0] == user_id for u in users)

    # Оновлення
    update_user(user_id, "Alice Updated", 26)
    users = get_users()
    assert any(u[0] == user_id and u[1] == "Alice Updated" for u in users)

    # Видалення
    delete_user(user_id)
    users = get_users()
    assert all(u[0] != user_id for u in users)

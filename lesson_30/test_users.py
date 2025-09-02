# Тести з Allure
import allure
import pytest
from db_utils import create_table, insert_user, update_user, delete_user, get_users

@allure.feature("User management - Insert")
def test_insert_user(db_connection):
    """
    Тест вставки користувача.
    """
    conn = db_connection
    with allure.step("Створюємо таблицю users"):
        create_table(conn)

    with allure.step("Вставляємо користувача Alice, 25 років"):
        user_id = insert_user(conn, "Alice", 25)

    with allure.step("Перевіряємо, що користувач доданий у таблицю"):
        users = get_users(conn)
        assert any(u[0] == user_id for u in users)

@allure.feature("User management - Update")
def test_update_user(db_connection):
    """
    Тест оновлення користувача.
    """
    conn = db_connection
    with allure.step("Створюємо таблицю users"):
        create_table(conn)

    with allure.step("Вставляємо користувача Bob, 30 років"):
        user_id = insert_user(conn, "Bob", 30)

    with allure.step("Оновлюємо користувача Bob -> Bob Updated, 31"):
        update_user(conn, user_id, "Bob Updated", 31)

    with allure.step("Перевіряємо, що дані користувача оновлені"):
        users = get_users(conn)
        assert any(u[0] == user_id and u[1] == "Bob Updated" and u[2] == 31 for u in users)

    with allure.step("Видаляємо тестового користувача"):
        delete_user(conn, user_id)

@allure.feature("User management - Delete")
def test_delete_user(db_connection):
    """
    Тест видалення користувача.
    """
    conn = db_connection
    with allure.step("Створюємо таблицю users"):
        create_table(conn)

    with allure.step("Вставляємо користувача Charlie, 40 років"):
        user_id = insert_user(conn, "Charlie", 40)

    with allure.step("Видаляємо користувача Charlie"):
        delete_user(conn, user_id)

    with allure.step("Перевіряємо, що користувача немає у таблиці"):
        users = get_users(conn)
        assert all(u[0] != user_id for u in users)

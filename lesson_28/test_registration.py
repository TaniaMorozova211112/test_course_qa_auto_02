import pytest
import time

def test_user_registration(fill_registration_form, check_success_message):
    unique_email = f"test{int(time.time())}@example.com"
    fill_registration_form("Test", "User", unique_email, "Qwerty123!")
    assert check_success_message(), "Success message not visible"

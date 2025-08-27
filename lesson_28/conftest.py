import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from registration_page import RegistrationPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    yield driver
    driver.quit()

@pytest.fixture
def registration_form(driver):
    def _registration_form():
        page = RegistrationPage(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(page.open_modal_button())
        ).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of(page.name_input())
        )
        return page
    return _registration_form

@pytest.fixture
def fill_registration_form(driver, registration_form):
    def _fill_form(firstname, lastname, email, password):
        page = registration_form()
        page.name_input().send_keys(firstname)
        page.lastname_input().send_keys(lastname)
        page.email_input().send_keys(email)
        page.password_input().send_keys(password)
        page.repeat_password_input().send_keys(password)
        page.register_button().click()
        return page
    return _fill_form

@pytest.fixture
def check_success_message(driver):
    def _check():
        page = RegistrationPage(driver)
        return WebDriverWait(driver, 10).until(
            EC.visibility_of(page.success_message())
        ).text
    return _check
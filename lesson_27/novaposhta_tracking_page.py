from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class NovaPoshtaTrackingPage:
    URL = "https://tracking.novaposhta.ua/#/uk"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        self.driver.maximize_window()
        self.driver.get(self.URL)

    def enter_tracking_number(self, tracking_number: str):
        """Вводить номер посилки і натискає 'Пошук'"""
        try:
            # поле для вводу
            input_field = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#en"))
            )
            input_field.clear()
            input_field.send_keys(tracking_number)

            # кнопка пошуку (вона стане активною після вводу)
            button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#np-number-input-desktop-btn-search-en"))
            )
            button.click()
        except TimeoutException:
            raise Exception("Не знайдено поле вводу або кнопку 'Пошук'")

    def get_tracking_status(self) -> str:
        """Повертає текст статусу відправлення"""
        try:
            status_element = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".header__status-text"))
            )
            return status_element.text.strip()
        except TimeoutException:
            raise Exception("Статус відправлення не знайдено")

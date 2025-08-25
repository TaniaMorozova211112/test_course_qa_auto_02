from selenium.webdriver.common.by import By

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def open_modal_button(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Sign up']")

    def name_input(self):
        return self.driver.find_element(By.ID, "signupName")

    def lastname_input(self):
        return self.driver.find_element(By.ID, "signupLastName")

    def email_input(self):
        return self.driver.find_element(By.ID, "signupEmail")

    def password_input(self):
        return self.driver.find_element(By.ID, "signupPassword")

    def repeat_password_input(self):
        return self.driver.find_element(By.ID, "signupRepeatPassword")

    def register_button(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            "body > ngb-modal-window > div > div > app-signup-modal > div.modal-footer > button.btn.btn-primary"
        )

    def success_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, "app-alert-list")

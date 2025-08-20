from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера
driver = webdriver.Chrome()
driver.maximize_window()

# Відкриваємо сторінку "Станьте партнером"
driver.get("https://wff.org.ua/partners/become")

# Очікування елементів
wait = WebDriverWait(driver, 10)

# Локатори для перевірки
locators = [
    (By.ID, "name"),
    (By.ID, "company"),
    (By.ID, "phone"),
    (By.ID, "text_for_help"),
    (By.ID, "policy"),
    (By.NAME, "name"),
    (By.NAME, "company"),
    (By.NAME, "phone"),
    (By.NAME, "text_for_help"),
    (By.NAME, "policy"),
    (By.TAG_NAME, "input"),
    (By.TAG_NAME, "button"),
    (By.TAG_NAME, "a"),
    (By.LINK_TEXT, "Політика конфіденційності"),
    (By.PARTIAL_LINK_TEXT, "Політикою"),
    (By.CSS_SELECTOR, "button.button_button__MFmXH.btn-primary-secondary"),
    (By.XPATH, "//a[text()='Політика конфіденційності']"),
]

# Відкриваємо файл для запису результатів
with open("results.txt", "w", encoding="utf-8") as file:
    for by, value in locators:
        try:
            wait.until(EC.presence_of_element_located((by, value)))
            result = f"Локатор {by}='{value}' знайдено!"
        except:
            result = f"Локатор {by}='{value}' не знайдено"
        print(result)
        file.write(result + "\n")

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск браузера
driver = webdriver.Chrome()
driver.maximize_window()

# Відкриваємо сторінку "Станьте партнером"
driver.get("https://wff.org.ua/partners/become")

# --- Локатори для форми ---
# By.ID
driver.find_element(By.ID, "name")          # Поле "Ім'я"
driver.find_element(By.ID, "company")       # Поле "Компанія"
driver.find_element(By.ID, "phone")         # Поле "Телефон"
driver.find_element(By.ID, "text_for_help") # Поле "Як можете допомогти"
driver.find_element(By.ID, "policy")        # Checkbox "Погоджуюсь з політикою"

# By.NAME
driver.find_element(By.NAME, "name")
driver.find_element(By.NAME, "company")
driver.find_element(By.NAME, "phone")
driver.find_element(By.NAME, "text_for_help")
driver.find_element(By.NAME, "policy")

# By.TAG_NAME
driver.find_element(By.TAG_NAME, "input")   # Перше поле вводу на сторінці
driver.find_elements(By.TAG_NAME, "button") # Всі кнопки на сторінці
driver.find_elements(By.TAG_NAME, "a")      # Всі посилання на сторінці

# By.LINK_TEXT / By.PARTIAL_LINK_TEXT
driver.find_element(By.LINK_TEXT, "Політика конфіденційності")  # Посилання на політику Футер
driver.find_element(By.PARTIAL_LINK_TEXT, "Політикою")          # Частина тексту посилання

# By.CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR, "button.button_button__MFmXH.btn-primary-secondary")  # Кнопка "Підтримати", Хедер

# By.XPATH
driver.find_element(By.XPATH, "//a[text()='Політика конфіденційності']")  # Посилання на політику

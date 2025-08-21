from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Запускаємо браузер
driver = webdriver.Chrome()
driver.maximize_window()

# Відкриваємо головну сторінку
driver.get("file:///C:/Users/tanib/clone_testgit_repo_01/test_course_qa_auto_02/lesson_26/dz.html")

# =========================
# Робота з першим фреймом
# =========================
driver.switch_to.frame("frame1")  # переходимо у фрейм1

# Вводимо правильний секрет
driver.find_element(By.ID, "input1").send_keys("Frame1_Secret")
driver.find_element(By.TAG_NAME, "button").click()

# Працюємо з alert
alert = Alert(driver)
assert alert.text == "Верифікація пройшла успішно!", "Перевірка у фреймі1 не пройшла!"
print("Frame1 OK:", alert.text)
alert.accept()  # закриваємо вікно

# Повертаємось назад на головну сторінку
driver.switch_to.default_content()

# =========================
# Робота з другим фреймом
# =========================
driver.switch_to.frame("frame2")  # переходимо у фрейм2

# Вводимо правильний секрет
driver.find_element(By.ID, "input2").send_keys("Frame2_Secret")
driver.find_element(By.TAG_NAME, "button").click()

# Працюємо з alert
alert = Alert(driver)
assert alert.text == "Верифікація пройшла успішно!", "Перевірка у фреймі2 не пройшла!"
print("Frame2 OK:", alert.text)
alert.accept()

# Завершуємо
time.sleep(2)
driver.quit()

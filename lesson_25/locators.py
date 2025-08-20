By.ID
# Пошук за унікальним значенням атрибуту id.
# Найшвидший і найстабільніший, якщо id не змінюється.
# driver.find_element(By.ID, "login-button")

driver.find_element(By.ID, "name")  # поле "Ім`я", форма для партнерів "Умови співпраці"
driver.find_element(By.ID, "company")  # поле "Компанія", форма для партнерів "Умови співпраці"
driver.find_element(By.ID, "phone")    # поле "Телефон", форма для партнерів "Умови співпраці"
driver.find_element(By.ID, "text_for_help")  # поле "Як можете допомогти", форма для партнерів "Умови співпраці"
driver.find_element(By.ID, "policy")   # checkbox (прапорець), форма для партнерів "Умови співпраці"

By.NAME
# Пошук за атрибутом name. Часто використовується для форм.
# driver.find_element(By.NAME, "username")

driver.find_element(By.NAME, "name")  # поле "Ім`я", форма для партнерів "Умови співпраці"
driver.find_element(By.NAME, "company")  # поле "Компанія", форма для партнерів "Умови співпраці"
driver.find_element(By.NAME, "phone")    # поле "Телефон", форма для партнерів "Умови співпраці"
driver.find_element(By.NAME, "text_for_help")  # поле "Як можете допомогти", форма для партнерів "Умови співпраці"
driver.find_element(By.NAME, "policy")   # checkbox (прапорець), форма для партнерів "Умови співпраці"


By.CLASS_NAME
# Пошук за атрибутом class. Добре, якщо клас унікальний.
# driver.find_element(By.CLASS_NAME, "btn-primary")

driver.find_element(By.CLASS_NAME, "btn-primary-secondary")  # За класом/Кнопка "Підтримати", Хедер
driver.find_element(By.CLASS_NAME, "h3")  # За класом/назва блоку "Культурні проєкти", секція "Як допомагаємо" Головна стр
driver.find_element(By.CLASS_NAME, "joinButton_button__HPJKt") # За класом/Кнопка "Долучитися" в проєкті "Барви життя" на сторінці "Усі проєкти"
driver.find_element(By.CLASS_NAME, "form_form_field_checkbox__hStKf")  # checkbox (прапорець), форма для партнерів "Умови співпраці"
driver.find_element(By.CLASS_NAME, "button_button__MFmXH")  # За класом/Кнопка "Стати партнером", сторінка "Партнери"
driver.find_element(By.CLASS_NAME, "photoReports_photo__JSce4")  # За класом/перше фото в фото-звіті, сторінка Проєкт "Теплі обійма"


By.TAG_NAME
# Пошук за тегом HTML (input, button, h1 тощо).
# driver.find_element(By.TAG_NAME, "h1")

driver.find_element(By.TAG_NAME, "img")   # За тегом/елемент "Logo", Хедер
driver.find_element(By.TAG_NAME, "h3")    # За тегом/назва блоку "Культурні проєкти", секція "Як допомагаємо" Головна стр
driver.find_element(By.TAG_NAME, "input")  # Перше поле вводу на сторінці
driver.find_elements(By.TAG_NAME, "button")  # Всі кнопки на сторінці
driver.find_elements(By.TAG_NAME, "a")  # Всі посилання на сторінці


By.LINK_TEXT
# Пошук за точним текстом у <a> (посиланні).
# driver.find_element(By.LINK_TEXT, "Sign In")

driver.find_element(By.LINK_TEXT, "UKR")   # по тексту/елемент "UKR", Хедер
driver.find_element(By.LINK_TEXT, "Проєкти")  # по тексту/ "Проєкти", Хедер
driver.find_element(By.LINK_TEXT, "Звіт ГО “Жінки за майбутнє країни” за 2023 рік")  # по тексту/посилання на звіт, сторінка "Звіти"
driver.find_element(By.LINK_TEXT, "Junfolio")  # по тексту/посилання на сайт "Junfolio", Футер
driver.find_element(By.LINK_TEXT, "Політика конфіденційності")  # по тексту/посилання "Політика конфіденційності", Футер



By.PARTIAL_LINK_TEXT
# Пошук за частиною тексту у посиланні.
# driver.find_element(By.PARTIAL_LINK_TEXT, "Sign")

driver.find_element(By.PARTIAL_LINK_TEXT, "Проєкт")  # по частині тексту/ "Проєкти", Хедер
driver.find_element(By.PARTIAL_LINK_TEXT, "Жінки за майбутнє")  # по частині тексту/посилання на звіт, сторінка "Звіти"
driver.find_element(By.PARTIAL_LINK_TEXT, "Junf")  # по частині тексту/посилання на сайт "Junfolio", Футер
driver.find_element(By.PARTIAL_LINK_TEXT, "Політика")   # по частині тексту/посилання "Політика конфіденційності", Футер
driver.find_element(By.PARTIAL_LINK_TEXT, "Політикою")  # по частині тексту/посилання "Політика конфіденційності", форма для партнерів "Умови співпраці"



By.CSS_SELECTOR
# Використання CSS-селекторів. Дуже гнучкий і швидкий метод.
# driver.find_element(By.CSS_SELECTOR, "form#login input[type='email']")

driver.find_element(By.CSS_SELECTOR, "img[alt='logo']")  # через атрибут alt="logo"/елемент "Logo", Хедер
driver.find_element(By.CSS_SELECTOR, "img[src*='organizationLogo']")  # унікальний початок атрибуту src/елемент "Logo", Хедер
driver.find_element(By.CSS_SELECTOR, "a[href='/']")    # через атрибут href/елемент "UKR", Хедер
driver.find_element(By.CSS_SELECTOR, "button.button_button__MFmXH.btn-primary-secondary")  # за повним класом/кнопка "Підтримати", Хедер
driver.find_element(By.CSS_SELECTOR, "svg.HowHelpSection_icon__3OuRF")   # за класом/іконка "Гуманітарна допомога", секція "Як допомагаємо" Головна стр



By.XPATH
# Використання XPath-запиту. Підтримує пошук за текстом, атрибутами, ієрархією.
# driver.find_element(By.XPATH, "//form[@id='login']//input[@type='email']")

driver.find_element(By.XPATH, "//img[@alt='logo']")   # через атрибут alt="logo"/елемент "Logo", Хедер
driver.find_element(By.XPATH, "//img[contains(@src,'organizationLogo')]")  # унікальний початок атрибуту src/елемент "Logo", Хедер
driver.find_element(By.XPATH, "//a[text()='UKR']")   # за текстом/елемент "UKR", Хедер
driver.find_element(By.XPATH, "//button[text()='Підтримати']")  # за текстом/кнопка "Підтримати", Хедер
driver.find_element(By.XPATH, "//svg[contains(@class, 'human-icon')]")  # по частині класу/іконка "Гуманітарна допомога", секція "Як допомагаємо" Головна стр
driver.find_element(By.XPATH, "//a[text()='Проєкти']")  # По тексту + тег/ "Проєкти", Хедер




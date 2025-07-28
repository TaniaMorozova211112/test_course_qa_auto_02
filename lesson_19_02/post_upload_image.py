# Цей файл надсилає зображення на сервер за допомогою HTTP-запиту POST на url /upload
# Імпортується бібліотека requests, яка дозволяє надсилати HTTP-запити
import requests


# Шлях до файлу, який будемо завантажити (test.jpg - наше фото, в тій же папці, де цей код)
image_path = 'test.jpg'

url = 'http://127.0.0.1:8080/upload'

# Відкриваємо файл у двійковому режимі (rb) і створюємо словник files,
# який потрібен requests.post для передачі файлу
with open(image_path, 'rb') as f:
    files = {'image': f}
    # Надсилається POST-запит з файлом на сервер
    response = requests.post(url, files=files)

# Виводиться код відповіді сервера
print('Код статусу:', response.status_code)
# Виводиться відповідь від сервера у форматі JSON
print('Відповідь сервера:', response.json())

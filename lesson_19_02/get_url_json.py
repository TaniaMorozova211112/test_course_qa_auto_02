# Отримання URL завантаженого зображення в форматі json
import requests


# Файл завантажено як test.jpg
filename = 'test.jpg'
# GET-запит треба надіслати на:
url = f'http://127.0.0.1:8080/image/{filename}'

# Заголовок Content-Type визначає тип відповіді:
# text - отримаємо JSON з URL
headers = {'Content-Type': 'text'}

response = requests.get(url, headers=headers)

print('Код статусу:', response.status_code)
print('Відповідь сервера:', response.json())

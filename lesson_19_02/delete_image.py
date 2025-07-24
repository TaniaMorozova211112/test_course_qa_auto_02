# Видалення зображення
import requests


filename = 'test.jpg'
url = f'http://127.0.0.1:8080/delete/{filename}'

response = requests.delete(url)

print('Код статусу:', response.status_code)
print('Відповідь сервера:', response.json())

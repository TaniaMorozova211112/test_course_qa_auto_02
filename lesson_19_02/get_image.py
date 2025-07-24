# Отримання завантаженого зображення
import requests


url = 'http://127.0.0.1:8080/image/test.jpg'

# Заголовок Content-Type визначає тип відповіді:
# image - отримаємо саме зображення
headers = {
    'Content-Type': 'image'
}

response = requests.get(url, headers=headers)

print(f"Статус-код відповіді: {response.status_code}")

if response.status_code == 200:
    with open('downloaded_test.jpg', 'wb') as f:
        f.write(response.content)
    print("Зображення збережено як downloaded_test.jpg")
else:
    print(f"Помилка: {response.status_code}")


import requests

# URL API NASA для фото ровера Curiosity
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

# Параметри запиту: день (sol), камера, API ключ
params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'  # безкоштовний ключ з обмеженням на кількість запитів
}

# Виконуємо GET-запит
response = requests.get(url, params=params)

# Перевіряємо статус відповіді
if response.status_code == 200:
    data = response.json()  # парсимо JSON у словник

    photos = data.get('photos', [])
    if not photos:
        print("Фото не знайдено.")
    else:
        print(f"Знайдено {len(photos)} фото. Завантажуємо...")

        for i, photo in enumerate(photos[:2], start=1):  # для прикладу беремо 2 фото
            img_url = photo.get('img_src')
            if img_url:
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    filename = f"mars_photo{i}.jpg"
                    with open(filename, 'wb') as f:
                        f.write(img_response.content)
                    print(f"Збережено {filename}")
                else:
                    print(f"Помилка завантаження фото {i}: статус {img_response.status_code}")
            else:
                print(f"Фото {i} не має посилання img_src.")
else:
    print(f"Помилка запиту: статус {response.status_code}")

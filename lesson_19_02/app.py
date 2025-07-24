from flask import Flask, request, jsonify, send_from_directory
import os


# Ініціалізуємо Flask-додаток
app = Flask(__name__)

# Вказуємо шлях до папки, де зберігатимуться завантажені файли
upload_directory = './uploads'

# Якщо теки uploads немає — створюємо її
if not os.path.exists(upload_directory):
    os.makedirs(upload_directory)

# Головна сторінка — перевірка роботи сервера
@app.route('/')
def index():
    # Повертаємо простий текст, щоб впевнитися, що сервер працює
    return 'Привіт! Сервер працює!'

# Маршрут для завантаження зображення методом POST
@app.route('/upload', methods=['POST'])
def upload_image():
    # Перевіряємо, чи є файл в запиті під ключем 'image'
    if 'image' not in request.files:
        # Якщо ні — повертаємо помилку 400 (Bad Request)
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']

    # Перевіряємо, що користувач вибрав файл (ім'я файлу не пусте)
    if image.filename == '':
        # Якщо ні — повертаємо помилку 400
        return jsonify({'error': 'No selected file'}), 400

    # Формуємо повний шлях для збереження файлу
    filename = os.path.join(upload_directory, image.filename)
    # Зберігаємо файл на диск у теці uploads
    image.save(filename)

    # Повертаємо JSON з URL завантаженого зображення і код 201 (Created)
    return jsonify({'image_url': request.host_url + 'uploads/' + image.filename}), 201

# Маршрут для отримання зображення за іменем файлу методом GET
@app.route('/image/<filename>', methods=['GET'])
def get_image(filename):
    # Отримуємо Content-Type з заголовків запиту
    content_type = request.headers.get('Content-Type')
    # Формуємо шлях до файлу
    filepath = os.path.join(upload_directory, filename)

    if os.path.exists(filepath):
        # Якщо клієнт просить текст — повертаємо JSON з посиланням на зображення
        if content_type == 'text':
            return jsonify({'image_url': request.host_url + 'uploads/' + filename}), 200
        # Якщо клієнт просить зображення — віддаємо файл
        elif content_type == 'image':
            return send_from_directory(upload_directory, filename)
        else:
            # Якщо Content-Type не підтримується — повертаємо помилку 400
            return jsonify({'error': 'Unsupported Content-Type'}), 400
    else:
        # Якщо файл не знайдено — повертаємо помилку 404
        return jsonify({'error': 'Image not found'}), 404

# Маршрут для видалення зображення за іменем файлу методом DELETE
@app.route('/delete/<filename>', methods=['DELETE'])
def delete_image(filename):
    filepath = os.path.join(upload_directory, filename)

    # Якщо файл не існує — повертаємо помилку 404
    if not os.path.exists(filepath):
        return jsonify({'error': 'Image not found'}), 404

    # Видаляємо файл з теки uploads
    os.remove(filepath)

    # Повертаємо повідомлення про успішне видалення файлу
    return jsonify({'message': f'Image {filename} deleted'}), 200

# Додатковий маршрут: обслуговування статичних файлів у папці uploads
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(upload_directory, filename)

# Запускаємо сервер, якщо цей файл запускається напряму
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
import os
import json
import logging

# Налаштування логера для запису помилок у файл
LOG_FILE = 'json__morozova.log'
logging.basicConfig(
    filename=LOG_FILE,
    filemode='a',  # додавати у файл
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.ERROR,
    encoding='utf-8'
)

# Шлях до папки з JSON файлами
current_dir = os.path.dirname(__file__)
json_dir = os.path.join(
    os.path.dirname(__file__),
    "..",
    "automation_qa", "ideas_for_test", "work_with_json"
) 

# Перевірка, чи папка існує
if not os.path.isdir(json_dir):
    raise FileNotFoundError(f"Папка не знайдена: {json_dir}")

# Обходимо всі файли у теці
for filename in os.listdir(json_dir):
    file_path = os.path.join(json_dir, filename)

    # Пропускаємо, якщо це не файл
    if not os.path.isfile(file_path):
        continue

    # Перевіряємо розширення — лише .json
    if not filename.lower().endswith('.json'):
        continue

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)  # Зчитуємо JSON з файлу
    except json.JSONDecodeError as e:
        # Якщо JSON невалідний — логування помилки з назвою файлу та описом помилки
        logging.error(f"Невалідний JSON у файлі {filename}: {e}")
    except Exception as e:
        # Логування інших помилок, наприклад, проблем з читанням файлу
        logging.error(f"Помилка при обробці файлу {filename}: {e}")

print(
    f"Перевірка файлів у {json_dir} завершена.\n"
    f"Помилки (якщо були) у {LOG_FILE}."
)
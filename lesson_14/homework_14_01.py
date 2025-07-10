import csv
import os

# Отримуємо корінь проєкту (текущий файл - назад на рівень вгору)
project_root = os.path.dirname(os.path.dirname(__file__))

# Формуємо шлях до теки з CSV-файлами
data_dir = os.path.join(
    project_root,
    'automation_qa', 'ideas_for_test', 'work_with_csv'
)

# Імена двох вхідних CSV-файлів
file1 = os.path.join(data_dir, 'random.csv')
file2 = os.path.join(data_dir, 'random-michaels.csv')

# Формуємо шлях до результатного файлу
result_file = os.path.join(
    os.path.dirname(__file__),
    'result_morozova.csv'
)

# Перевіряємо, чи існують обидва файли
if not os.path.exists(file1):
    raise FileNotFoundError(f"Файл не знайдено: {file1}")

if not os.path.exists(file2):
    raise FileNotFoundError(f"Файл не знайдено: {file2}")

# Створюємо множину (set) для унікальних рядків з обох файлів
unique_rows = set()

# Зчитуємо кожен файл окремо
for path in [file1, file2]:
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            unique_rows.add(tuple(row))  # Кортеж додається у множину (унікальність)

# Записуємо унікальні рядки у файл результату
with open(result_file, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    for row in sorted(unique_rows):  # Сортуємо для зручності
        writer.writerow(row)

# Виводимо повідомлення про успішне завершення
print(f"Унікальні рядки з обох файлів записано в: {result_file}")
print(f"Загальна кількість рядків у результаті: {len(unique_rows)}")


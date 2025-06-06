# рахуємо символи, які присутні тільки один раз

user_input = input("Введи рядок: ")

# прибираємо всі пробіли з рядка
user_input_clear = user_input.replace(" ", "")

# створюємо словник для підрахунку кількості кожного символу
symbol_counts = {}

# рахуємо скільки разів зустрічається кожен символ
for symbol in user_input_clear:
    if symbol in symbol_counts:
        symbol_counts[symbol] += 1
    else:
        symbol_counts[symbol] = 1

# рахуємо кількість символів, які зустрічаються тільки один раз
unique_once_count = 0
for count in symbol_counts.values():
    if count == 1:
        unique_once_count += 1

if unique_once_count > 10:
    print(True)
else:
    print(False)


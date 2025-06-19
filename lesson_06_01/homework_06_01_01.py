# рахуємо всі унікальні символи

user_input = input("Введи рядок: ")

# прибираємо пробіли
user_input_clear = user_input.replace(" ", "")

# створюємо множину унікальних символів
unique_symbols = set(user_input_clear)

if len(unique_symbols) > 10:
    print("True")
else:
    print("False")

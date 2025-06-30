# функція 1
# підраховує скільки грошей знадобиться для купівлі
# всього продукту в кількості "amt" по ціні за 1шт "price"

def check(amt, price):
    if not isinstance(amt, (int, float)) or not isinstance(price, (int, float)):
        raise TypeError("Аргументи повинні бути числами (int або float)")

    if amt < 0 or price < 0:
        raise ValueError("Кількість та ціна не можуть бути від'ємними")

    return amt * price


# функція 2
# перевірка логіці на від'ємне значення та нуль
def check_total_str(total_str):
    if not isinstance(total_str, int):
        raise TypeError("Кількість рядків має бути цілим числом")
    if total_str <= 0:
        raise ValueError("Кількість рядків має бути більше нуля")


# функція 3
# обчислення суми чисел у рядку
def sum_numbers_from_string(number_string):
    try:
        numbers = [int(x.strip()) for x in number_string.split(",")]
        return str(sum(numbers)) # повертаємо як рядок
    except ValueError:
        return f'"Не можу це зробити"'




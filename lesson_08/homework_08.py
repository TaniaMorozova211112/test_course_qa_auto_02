# перевірка логіці на від'ємне значення та нуль
def check_total_str(total_str):
    if total_str <= 0:
        raise ValueError("Кількість строк має бути більше нуля")

while True:
    user_input = input("Введіть кількість строк: ").strip()

    if not user_input:
        print("Поле не може бути порожнім.")
        continue  # повертає до початку циклу

    try:
        total_str = int(user_input) # input() дає рядок
        check_total_str(total_str)
        break  # вихід із циклу, якщо все добре
    except ValueError as ve:
        if "більше нуля" in str(ve):
            print(f"Помилка логіки: {ve}")
        else:
            print("Ви ввели не ціле число.")
        continue  # повертає до початку циклу


# створюємо список рядків
list_all_str = []
for i in range(1, total_str + 1):
    user_input = input(f"Рядок {i}. Введіть числа через кому: ")
    list_all_str.append(user_input)


# функція для обчислення суми чисел у рядку
def sum_numbers_from_string(number_string):
    try:
        numbers = [int(x.strip()) for x in number_string.split(",")]
        return str(sum(numbers)) # повертаємо як рядок, буде далі потрібно для .join()
    except ValueError:
        return f'"Не можу це зробити"'


# обчислення сум та виведення результатів одним рядком через кому
print("\nРезультати:")

lst_sum = []
for number_string in list_all_str:
    result = sum_numbers_from_string(number_string)
    lst_sum.append(result)
print(", ".join(lst_sum))












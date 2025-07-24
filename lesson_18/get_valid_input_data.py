# Перевірка введення одного цілого числа
def get_valid_int(prompt, *, allow_zero=True, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))

            if not allow_zero and value == 0:
                print("Нуль не дозволено.")
                continue

            if min_value is not None and value < min_value:
                print(f"Значення має бути не менше {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Значення має бути не більше {max_value}.")
                continue

            return value

        except ValueError:
            print("Помилка: введіть одне ціле число!")


# Перевірка введення списку цілих чисел
def get_valid_int_list(prompt):
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("Ви нічого не ввели. Спробуйте ще раз.")
                continue

            parts = user_input.split()
            numbers = list(map(int, parts))

            if not numbers:
                print("Введіть хоча б одне число.")
                continue

            # Перевірка: чи всі числа == 0
            if all(n == 0 for n in numbers):
                print("Усі числа дорівнюють 0. Введіть хоча б одне ненульове число.")
                continue

            return numbers

        except ValueError:
            print("Помилка: введіть лише цілі числа через пробіл!")

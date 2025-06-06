user_input = input("Введи числа через пробіл: ").strip()

if user_input == '':
    print("Список порожній.")
else:
    # робимо список з усіх даних
    numbers_list = user_input.split()

    # робимо список тільки цілих чисел
    numbers_int_list = []
    for number in numbers_list:
        try:
            number_int = int(number)
            numbers_int_list.append(number_int)
        except ValueError:
            # якщо не вдалося перетворити на int — пропускаємо
            pass

    # рахуємо суму усіх ПАРНИХ чисел (позитивні, нуль та негативні)
    sum_even_numbers = 0
    for number in numbers_int_list:
        if number % 2 == 0:
            sum_even_numbers += number

    print(f'Сума всіх "ПАРНИХ" чисел: {sum_even_numbers:,}.'.replace(',', ' '))


# Імпортуємо функції перевірки валідних вхідних даних для одного числа та списку
from get_valid_input_data import get_valid_int, get_valid_int_list


# Розподіл інфо в консолі перед викликом наступної функції
def split_console():
    print("-"*100)


# Генератори:
# 1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def get_even_numbers(n_1):
    for number in range(0, n_1 + 1):
        if number % 2 == 0:
            yield number

n_1 = get_valid_int("Введіть максимальне значення послідовності (включно): ",
                    allow_zero=False, min_value=2)
for num in get_even_numbers(n_1):
    print(num)


# 2. Створіть генератор, який генерує послідовність Фібоначчі до певного числа N

# Розподіл інфо в консолі перед викликом наступної функції
split_console()

def get_fibonacci_numbers(n_2):
    a, b = 0, 1
    while a <= n_2:
        yield a
        a, b = b, a + b

n_2 = get_valid_int("\nВведіть число, "
                    "до якого генерувати послідовність Фібоначчі: ", min_value=0)
for numb in get_fibonacci_numbers(n_2):
    print(numb)


# Ітератори:
# 1a. Реалізуйте ітератор для зворотного виведення елементів списку.

# Розподіл інфо в консолі перед викликом наступної функції
split_console()

# Зчитуємо весь рядок чисел, розділених пробілом
list_input = get_valid_int_list(
    "\nРеалізуємо ітератор для зворотного виведення елементів списку."
    "\nМетод N1."
    "\nВведіть список чисел через пробіл: "
)

# Створюємо ітератор для зворотного порядку
reverse_iterator = iter(list_input[::-1])

# Виводимо елементи за допомогою ітератора
for item in reverse_iterator:
    print(item)


# 1b. Реалізуйте ітератор для зворотного виведення елементів списку (за допомогою класів).

# Розподіл інфо в консолі перед викликом наступної функції
split_console()

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)  # починаємо з позиції за останнім індексом

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration  # кінець ітерації
        self.index -= 1
        return self.data[self.index]

# Зчитуємо весь рядок чисел, розділених пробілом

# input_list= list(map(int, input(
#     '\nРеалізуємо ітератор для зворотного виведення елементів списку.'
#     '\nМетод N2.'
#     '\nВведіть список чисел через пробіл: ').split()))
input_list = get_valid_int_list(
    "\nРеалізуємо ітератор для зворотного виведення елементів списку."
    "\nМетод N2."
    "\nВведіть список чисел через пробіл: "
)

reverse_iter = ReverseIterator(input_list)

for i in reverse_iter:
    print(i)


# 2a. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N
# (за допомогою класів).

# Розподіл інфо в консолі перед викликом наступної функції
split_console()

class EvenIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.max_value:
            if self.current % 2 == 0:
                value = self.current
                self.current += 1
                return value
            self.current += 1
        raise StopIteration

# Ввод максимального значення діапазону (включно)

# n_3 = int(input(
#     '\nРеалізуємо ітератор, який повертає всі парні числа в діапазоні від 0 до N.'
#     '\nВведіть максимальне значення діапазону (включно): '))

n_3 = get_valid_int(
    "\nРеалізуємо ітератор, який повертає всі парні числа в діапазоні від 0 до N."
    "\nВведіть максимальне значення діапазону (включно): ", allow_zero=False, min_value=2
)

even_iter = EvenIterator(n_3)

for number_even in even_iter:
    print(number_even)


# Декоратори:
# 1. Напишіть декоратор, який логує аргументи та результати викликаної функції.

# Розподіл інфо в консолі перед викликом наступної функції
split_console()

print("\nРеалізуємо декоратор, який логує аргументи та результати викликаної функції.")

def log_arguments_and_result(func):
    def wrapper(*args, **kwargs):
        print(f"\nВиклик функції: {func.__name__}")
        print(f"Аргументи: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@log_arguments_and_result
def multiply(a, b):
    return a * b

@log_arguments_and_result
def greet(name="Гість"):
    return f"Привіт, {name}!"

# Виклики:
multiply(3, 4)
greet(name="Тетяна")


# 2. Створюємо декоратор, який перехоплює та обробляє винятки,
# які виникають в ході виконання функції.

# Розподіл інфо в консолі перед викликом наступної функції
split_console()

print("\nРеалізуємо декоратор, який перехоплює та обробляє винятки, "
      "які виникають в ході виконання функції.")

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"\nВиникла помилка у функції '{func.__name__}': {e}")
            return None  # Явно повертаємо None, якщо виникла помилка
    return wrapper

@handle_exceptions
def divide(a, b):
    return a / b

result = divide(10, 0)

if result is not None:
    print(f"\nРезультат ділення: {result}")
    # Можна далі щось робити з result
else:
    print("\nОперація не виконана через помилку.")





























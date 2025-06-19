# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_of_two(var_1, var_2):
    """
    Обчислює суму двох чисел і повертає її у форматованому рядку.

    Аргументи:
    var_1 (int або float): Перше число.
    var_2 (int або float): Друге число.

    Повертає:
    str: Рядок з результатом додавання у вигляді:
    'Сума чисел {var_1} та {var_2} дорівнює {total_sum}.'
    """
    total_sum = var_1 + var_2
    return f'Сума чисел {var_1} та {var_2} дорівнює {total_sum}.'


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def arithmetic_mean(lst_inp):
    """
    Обчислює середнє арифметичне чисел у списку.

    Аргументи:
    lst_inp (list): Список чисел (int або float).

    Повертає:
    float: Середнє арифметичне значення списку.
    str: Повідомлення про помилку, якщо список порожній або містить нечислові елементи.
    """
    if not lst_inp:
        return 'Помилка: список порожній.'
    if not all(isinstance(x, (int, float)) for x in lst_inp):
        return 'Помилка: список має містити лише числа.'
    result = sum(lst_inp) / len(lst_inp)
    return result


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def revers_str(s):
    """
    Повертає рядок у зворотному порядку.

    Аргументи:
    s (str): Рядок, який потрібно перевернути.

    Повертає:
    str: Рядок, записаний у зворотному порядку.
    """
    str_revers = s[::-1]
    return str_revers


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word_in_the_list(list_words):
    """
    Повертає найдовше слово зі списку слів.

    Аргументи:
    list_words (list): Список рядків (слів), у якому шукається найдовше слово.

    Повертає:
    str: Слово з максимальною довжиною.
    Якщо список порожній — повертає повідомлення про помилку.
    """
    if not list_words:
        return 'Помилка: список порожній.'

    return max(list_words, key=len)


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    """
    Повертає індекс першого входження рядка str2 у рядок str1.
    Якщо str2 не знайдено, повертає -1.

    Аргументи:
    str1 (str): Рядок, у якому шукаємо.
    str2 (str): Рядок, який шукаємо.

    Повертає:
    int: Індекс першого входження або -1.
    """
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


# task 7
# Знайди остачу від діленя чисел:Add commentMore actions
# a) 8019 : 8     d) 7248 : 6
# b) 9907 : 9     e) 7128 : 5
# c) 2789 : 5     f) 19224 : 9

def remainder_from_division(dividend, divisor):
    """
    Обчислює та виводить остачу від ділення чисел.

    Аргументи:
    dividend (int): Ділене.
    divisor (int): Дільник.

    Повертає:
    None
    """
    remainder = dividend % divisor
    print(f'Остача від ділення {dividend} на {divisor}: {remainder}.')

remainder_from_division(dividend=8019, divisor=8)
remainder_from_division(dividend=9907, divisor=9)
remainder_from_division(dividend=2789, divisor=5)
remainder_from_division(dividend=7248, divisor=6)
remainder_from_division(dividend=7128, divisor=5)
remainder_from_division(dividend=19224, divisor=9)


# task 8
# Іринка, готуючись до свого дня народження, склала список того,Add commentMore actions
# що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
# для даного її замовлення.
# Назва товару    Кількість   Ціна
# Піца велика     4           274 грн
# Піца середня    2           218 грн
# Сік             4           35 грн
# Торт            1           350 грн
# Вода            3           21 грн

def check(amt, price):
    """
    Обчислює вартість товару за заданою кількістю та ціною одиниці.

    Аргументи:
    amt (int): Кількість одиниць товару.
    price (int): Ціна однієї одиниці товару в гривнях.

    Повертає:
    int: Загальна вартість товару.
    """
    total_price = amt * price
    return total_price

total_sum = (
    check(4, 274) +  # Піца велика
    check(2, 218) +  # Піца середня
    check(4, 35)  +  # Сік
    check(1, 350) +  # Торт
    check(3, 21)     # Вода
)

print(f"Для даного замовлення знадобиться: {total_sum:,} грн.".replace(',', ' '))


# task 9
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""

def total_trees_in_garden(apples, pear_difference, plum_difference):
    """
    Обчислює загальну кількість дерев у саду.

    Аргументи:
    apples (int): Кількість яблунь.
    pear_difference (int): На скільки груш більше, ніж яблунь.
    plum_difference (int): На скільки слив менше, ніж яблунь.

    Повертає:
    int: Загальна кількість дерев.
    """
    pears = apples + pear_difference
    plums = apples - plum_difference
    return apples + pears + plums

print("Всього дерев у саду:", total_trees_in_garden(4, 5, 2))


# task 10
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

def computer_price(total_months: int, monthly_payment: float):
    """
    Обчислює загальну вартість комп'ютера при оплаті частинами.

    Аргументи:
    total_months (int): Кількість місяців оплати.
    monthly_payment (float): Щомісячна сума платежу в гривнях.

    Повертає:
    float: Загальна вартість комп'ютера.
    """
    price = total_months * monthly_payment
    return price

total_months = 18
monthly_payment = 1179

# Виклик функції
price_computer = computer_price(total_months, monthly_payment)

print(
    f"Вартість комп’ютера: "
    f"{price_computer:,.2f}".replace(",", " ")
                            .replace(".", ",") +
    " грн."
)




"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
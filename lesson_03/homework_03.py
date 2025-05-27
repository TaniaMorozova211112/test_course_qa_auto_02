alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where -" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n" - so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії

alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where -" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '" - so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)


# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# екранувала всі символи одинарної лапки в task 01

list_character = []

for character in alice_in_wonderland:
    if character == "'":
        list_character.append(character) 

print(
    f"Символи одинарної лапки (') у тексті: {list_character}.\n"
    f"Всього символів (') у тексті: {len(list_character)}."
)


# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
    # Площа Чорного моря становить 436 402 км2, а площа Азовського
    # моря становить 37 800 км2. Яку площу займають Чорне та Азов-
    # ське моря разом?
"""

black_sea_area = 436_402
sea_of_azov_area = 37_800

total_area = black_sea_area + sea_of_azov_area

print(f"Чорне та Азовське моря разом займають: {total_area:,} км2.".replace(',', ' '))


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_goods = 375_291
first_plus_second_warehouses = 250_449
second_plus_third_warehouses = 222_950

first_warehouses = total_goods - second_plus_third_warehouses
third_warehouses = total_goods - first_plus_second_warehouses
second_warehouses = total_goods - first_warehouses - third_warehouses

print(f"На першому складі розміщено: {first_warehouses:,} товарів.\n\
На другому складі розміщено: {second_warehouses:,} товарів.\n\
На третьому складі розміщено: {third_warehouses:,} товарів.".replace(',', ' '))


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

total_months = 18
price_for_one_month_uah = 1179

price_computer = total_months * price_for_one_month_uah

print(f"Вартість комп’ютера: {price_computer:,.2f} ".replace(",", " ").replace(".", ",") + "грн.")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

print('a) Остача від діленя  8019 на 8:   ', 8019 % 8)
print('b) Остача від діленя  9907 на 9:   ', 9907 % 9)
print('c) Остача від діленя  2789 на 5:   ', 2789 % 5)
print('d) Остача від діленя  7248 на 6:   ', 7248 % 6)
print('e) Остача від діленя  7128 на 5:   ', 7128 % 5)
print('f) Остача від діленя 19224 на 9:   ', 19224 % 9)


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

def check(amt, price):
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


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

total_photo = 232
one_page_limit_photos = 8

if total_photo % one_page_limit_photos == 0:
    total_page = total_photo // one_page_limit_photos
else:
    total_page = total_photo // one_page_limit_photos + 1

print(f"Щоб вклеїти всі фото Ігорю знадобиться {total_page} сторінок.")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

total_distance_km = 1600
every_100_km_liters = 9
limit_petrol_tank_liters = 48

# Загальна кількість літрів бензину, необхідна для подорожі
total_petrol_liters = total_distance_km * every_100_km_liters // 100

# Кількість разів треба мати повний бак
number_of_times = (total_petrol_liters + limit_petrol_tank_liters - 1) // limit_petrol_tank_liters

# "-1" так як родина могла виїхати з повним баком
actual_stops = number_of_times - 1

print(
    f"1) Для подорожі із Харкова в Будапешт знадобиться {total_petrol_liters} літрів бензину.\n" 
    f"2) Якщо кожного разу заправляти повний бак, родині необхідно заїхати на заправку "
    f"щонайменше {actual_stops} рази під час цієї подорожі."
)

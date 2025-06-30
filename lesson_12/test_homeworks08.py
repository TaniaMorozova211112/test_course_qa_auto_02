# Імпорт бібліотеки
import unittest

# імпорт функцій, для яких робимо автотести, з модуля/файла "homeworks.py"
# (лежить в тій самій папці "lesson_12" що й тести)
# якщо в іншій папці: from назва_папки.назва_файлу import назва_ф-ції
from homeworks import check, check_total_str, sum_numbers_from_string


# 1. cтворення класу тестування для функціі "check"
class TestCheckFunction(unittest.TestCase):

    # визначення тестів
    def test_check_positive(self):  # перевірка множення позитивних цілих чисел
        result = check(2, 3)
        expected = 6
        self.assertEqual(
            result, expected,
            msg=f"[test_check_positive] Очікували {expected}, отримали {result}."
        )

    def test_check_result_is_number(self):  # перевірка, що функція повертає число (int, float)
        result = check(2.5, 4)
        self.assertIsInstance(
            result, (int, float),
            msg=f"[test_check_result_is_number] "
                f"Очікували число, отримали {type(result).__name__}."
        )

    def test_check_with_zero(self):  # перевірка множення на "0"
        result = check(0, 5)
        expected = 0
        self.assertEqual(
            result, expected,
            msg=f"[test_check_with_zero] "
                f"Очікували {expected} при множенні на '0', але отримали {result}."
        )

    def test_check_with_float(self):  # перевірка множення плаваючих чисел
        result = check(2.5, 4.5)
        expected = 11.25
        self.assertAlmostEqual(
            result, expected,
            msg=f"[test_check_with_float] Очікували {expected}, отримали {result}."
        )


    def test_check_with_large_numbers(self): # перевірка множення великих значень
        result = check(10000, 10000)
        expected = 100000000
        self.assertEqual(
            result, expected,
            msg=f"[test_check_with_large_numbers] "
                f"Помилка при роботі з великими числами. "
                f"Очікували {expected}, але отримали {result}."
        )

    def test_check_with_negative_amount(self):  # поява ValueError при відʼємній кількості
        with self.assertRaises(ValueError,
                               msg="[test_check_with_negative_amount] "
                                   "Має бути ValueError для від'ємної кількості."):
            check(-1, 10)

    def test_check_with_negative_price(self):  # поява ValueError при відʼємній ціні
        with self.assertRaises(ValueError,
                               msg="[test_check_with_negative_price] "
                                   "Має бути ValueError для від'ємної ціни."):
            check(3, -10)

    def test_check_with_string_argument(self):  # поява TypeError при неправильному типі
        with self.assertRaises(TypeError,
                               msg="[test_check_with_string_argument] "
                                   "Має бути TypeError для рядка як аргументу."):
            check("3", 2)


# запуск тестів
if __name__ == '__main__':
    unittest.main(verbosity=2)



# 2. cтворення класу тестування для функціі "check_total_str"
class TestCheckTotalStrFunction(unittest.TestCase):

    # визначення тестів
    # перевірка що функція нічого не повертає (none)
    def test_valid_positive_value_none(self):
        result = check_total_str(10)
        self.assertIsNone(result, "[test_valid_positive_value_none] Очікували 'None'.")

    # перевіряємо, що позитивне значення не викликає помилку
    def test_valid_positive_value(self):
        # try-except у позитивному тесті, бо функція нічого не повертає
        try:
            check_total_str(5)
        except Exception as e:
            self.fail(f"[test_valid_positive_value] "
                      f"Не очікували винятку, але отримали: {e}")

    def test_not_int_input_raises_type_error(self):  # поява TypeError при type != 'int'
        with self.assertRaises(TypeError,
                               msg="[test_not_int_input_raises_type_error] "
                                   "Очікували TypeError для всіх інших типів, окрім 'int'."):
            check_total_str(5.5)

    def test_zero_raises_value_error(self):  # поява ValueError при zero
        with self.assertRaises(ValueError,
                               msg="[test_zero_raises_value_error] "
                                   "Очікували ValueError для '0'."):
            check_total_str(0)

    def test_negative_raises_value_error(self):  # поява ValueError при відʼємному значенні
        with self.assertRaises(ValueError,
                               msg="[test_negative_raises_value_error] "
                                   "Очікували ValueError для '-3'."):
            check_total_str(-3)


# запуск тестів
if __name__ == '__main__':
    unittest.main(verbosity=2)


# 3. cтворення класу тестування для функціі "sum_numbers_from_string"
class TestSumNumbersFromString(unittest.TestCase):

    # визначення тестів
    def test_sum_valid_numbers(self):             # перевірка обробки валідного рядка чисел
        result = sum_numbers_from_string("1, 2, 3")
        self.assertEqual(result, "6",
                         "[test_sum_valid_numbers] Очікуємо суму '6'.")

    def test_sum_single_number(self):             # перевірка обробки рядка з одним числом
        result = sum_numbers_from_string("10")
        self.assertEqual(result, "10",
                         "[test_sum_single_number] Очікуємо '10'.")

    def test_sum_with_spaces(self):               # перевірка обробки пробілів у рядку
        result = sum_numbers_from_string(" 4 , 5 ,6 ")
        self.assertEqual(result, "15",
                         "[test_sum_with_spaces] Очікуємо суму '15'.")

    def test_invalid_string_returns_error(self):  # перевірка обробки невалідних значень
        result = sum_numbers_from_string("1, two, 3")
        self.assertEqual(result,
                         '"Не можу це зробити"',
                         f"[test_invalid_string_returns_error] "
                              f"Очікуємо повідомлення про помилку.")

    def test_empty_string_returns_error(self):    # перевірка обробки порожнього рядка
        result = sum_numbers_from_string("")
        self.assertEqual(result,
                         '"Не можу це зробити"',
                         f"[test_empty_string_returns_error] "
                              f"Очікуємо повідомлення про помилку.")

    def test_large_numbers(self):                  # перевірка обробки великих значень
        result = sum_numbers_from_string("1000000, 2000000")
        self.assertEqual(result,
                         "3000000",
                         "[test_large_numbers] Очікуємо суму '3000000'.")


# запуск тестів
if __name__ == "__main__":
    unittest.main(verbosity=2)


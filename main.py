def remainder(dividend, divisor):
    if divisor == 0:
        raise ValueError("Деление на ноль невозможно")
    return dividend % divisor


import unittest

#Тесты с использованием unittest:
class TestMath(unittest.TestCase):

    # Тест на корректный результат для положительных чисел
    def test_positive_numbers(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(25, 5), 0)

    # Тест на корректный результат для отрицательных чисел
    def test_negative_numbers(self):
        self.assertEqual(remainder(-10, 3), -1)
        self.assertEqual(remainder(10, -3), 1)
        self.assertEqual(remainder(-10, -3), -1)

    # Тест на корректный результат для нулевого делимого
    def test_zero_dividend(self):
        self.assertEqual(remainder(0, 3), 0)

    # Тест на исключение при делении на ноль
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            remainder(10, 0)
        with self.assertRaises(ValueError):
            remainder(0, 0)

    # Тест на остаток при делении нуля на ненулевое число
    def test_zero_mod_non_zero(self):
        self.assertEqual(remainder(0, 5), 0)


if __name__ == '__main__':
    unittest.main()

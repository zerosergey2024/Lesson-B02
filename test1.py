def count_vowels(s):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count

import pytest
def test_count_vowels():
    # Тест 1: обычная строка с гласными и согласными
    assert count_vowels("Привет") == 2

    # Тест 2: строка без гласных
    assert count_vowels("бгрш") == 0

    # Тест 3: пустая строка
    assert count_vowels("") == 0

    # Тест 4: строка с заглавными и строчными гласными
    assert count_vowels("AaEeIiOoUu") == 10

    # Тест 5: строка с заглавными и строчными гласными, строка с ошибкой
    assert count_vowels("AaEeIiOКoUu") == 11


# Запускаем тесты
test_count_vowels()
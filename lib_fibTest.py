import pytest
import lib

# Тестинг функции, возвращающей последовательность чисел Фибоначчи

# Позитивный тест
def test_fibPositive():
    assert lib.fib(6) == [1, 1, 2, 3, 5, 8]

# Негативный тест
def test_fibNegative():
    assert lib.fib(5) == [1, 1, 2, 3, 5, 8]




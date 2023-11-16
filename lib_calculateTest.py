import pytest
import lib

def test_calculatePositive1():
    assert lib.calculate(2, 3, '+') == 5
def test_calculatePositive2():
    assert lib.calculate(2, 3, '-') == -1
def test_calculatePositive3():
    assert lib.calculate(2, 3, '*') == 6
def test_calculatePositive4():
    assert lib.calculate(6, 3, '/') == 2
def test_calculateNegative():
    assert lib.calculate(6, 3, '/') == 3
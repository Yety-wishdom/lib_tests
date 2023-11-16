import pytest
import lib

def test_bubbleSortPositive():
    assert lib.bubbleSort([3, 1, 2, 4, 7, 6, 5]) == [1, 2, 3, 4, 5, 6, 7]
def test_bubbleSortNegative():
    assert lib.bubbleSort([3, 1, 2, 4, 7, 6, 5]) == [1, 3, 2, 4, 5, 6, 7]
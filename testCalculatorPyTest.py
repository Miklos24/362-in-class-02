import calculator
import pytest

def test_add_basic():
    assert calculator.add(2, 3) == 5

def test_add_val_error():
    with pytest.raises(ValueError):
        calculator.add("fish", 3)
    
def test_subtract_basic():
    assert calculator.subtract(3, 2) == 1

def test_subtract_neg():
    assert calculator.subtract(2, 3) == -1

def test_multiply_basic():
    assert calculator.multiply(2, 3) == 6

def test_multiply_list():
    assert calculator.multiply(2, [2, 3]) == [4, 6]

def test_divide_basic():
    assert calculator.divide(8, 4) == 2

def test_divide_float():
    assert calculator.divide(5, 2) == 2.5
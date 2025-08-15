MOCK_TEST = """
import pytest
from sample_code.calc import somar, subtrair, multiplicar, dividir

def test_addition():
    assert addition(2, 3) == 5, "Expected 2 + 3 to equal 5"

def test_subtraction():
    assert subtraction(5, 2) == 3, "Expected 5 - 2 to equal 3"

def test_multiplication():
    assert multiplication(4, 3) == 12, "Expected 4 * 3 to equal 12"

def test_division():
    assert division(10, 2) == 5, "Expected 10 / 2 to equal 5"

def test_division_by_zero():
    with pytest.raises(ValueError):
        division(10, 0)
"""

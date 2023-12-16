import pytest
from src import UnitTest
#fibonacci_numbers, bubble_sort, calculator
#UnitTest


# Тестирование функции fibonacci_numbers
class TestSorted:
    def test_fibonacci_numbers_valid_input(self):
        assert UnitTest.fibonacci_numbers(5) == [0, 1, 1, 2, 3]

    def test_fibonacci_numbers_zero_input(self):
        assert UnitTest.fibonacci_numbers(0) == []

    # Тестирование функции bubble_sort

    def test_bubble_sort_valid_input(self):
        assert UnitTest.bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    def test_bubble_sort_empty_input(self):
        assert UnitTest.bubble_sort([]) == []

    # Тестирование функции calculator

    def test_calculator_addition(self):
        assert UnitTest.calculator(2, 3, '+') == 5

    def test_calculator_subtraction(self):
        assert UnitTest.calculator(5, 3, '-') == 2

    def test_calculator_multiplication(self):
        assert UnitTest.calculator(2, 4, '*') == 8

    def test_calculator_division(self):
        assert UnitTest.calculator(8, 4, '/') == 2

    def test_calculator_division_by_zero(self):
        with pytest.raises(ValueError, match="Деление на ноль не допускается"):
            UnitTest.calculator(8, 0, '/')
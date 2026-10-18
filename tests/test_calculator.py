import unittest

from backend.calculator import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    power,
    calculate,
)

from backend.exceptions import (
    DivisionByZeroError,
    InvalidOperationError,
)


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(DivisionByZeroError):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)

    def test_modulus_by_zero(self):
        with self.assertRaises(DivisionByZeroError):
            modulus(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_calculate(self):
        self.assertEqual(
            calculate(10, 5, "add"),
            15,
        )

    def test_invalid_operation(self):
        with self.assertRaises(InvalidOperationError):
            calculate(10, 5, "square")


if __name__ == "__main__":
    unittest.main()
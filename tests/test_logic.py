import unittest
from operators import add, subtract, multiply, divide
from app import calculate

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 4), 2.5)
        
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_calculate_valid(self):
        self.assertEqual(calculate("10 + 5"), 15)

    def test_calculate_invalid_format(self):
        with self.assertRaises(ValueError):
            calculate("10 + 5 + 2")

    def test_calculate_non_numeric(self):
        with self.assertRaises(ValueError):
            calculate("10 + abc")

if __name__ == '__main__':
    unittest.main()
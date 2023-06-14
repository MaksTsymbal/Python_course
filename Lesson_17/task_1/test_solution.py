import unittest
from solution import calculate_squared_divided

class TestCalculateSquaredDivided(unittest.TestCase):

    def test_valid_input(self):
        result = calculate_squared_divided(4, 2)
        self.assertEqual(result, 8.0)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            calculate_squared_divided(4, 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate_squared_divided("four", 2)

if __name__ == '__main__':
    unittest.main()

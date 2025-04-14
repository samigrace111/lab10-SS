# https://github.com/samigrace111/lab10-SS
# Partner 1: Samantha Sobrino
# Partner 2: Samantha Sobrino

import unittest
from calculator import *   # imports add, subtract, multiply, divide, mul, div, logarithm, exp, hypotenuse, square_root

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        # Our 'div' function returns a string if dividing by zero
        self.assertEqual(div(5, 0), "Error: Cannot divide by zero")

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(8, 2), 3)
        self.assertAlmostEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(27, 3), 3)

    def test_log_invalid_base(self):  # 1 assertion
        # use same technique from test_divide_by_zero
        # but here we expect ValueError from invalid base
        with self.assertRaises(ValueError):
            logarithm(8, 1)

    ##########################
    
    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-1, 8), -8)

    def test_divide(self):  # 3 assertions
        # This uses 'divide', which returns a string if dividing by zero
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(5, 0), "Error: Cannot divide by zero")

    def test_log_invalid_argument(self):  # 1 assertion
        # call log function inside with invalid argument
        with self.assertRaises(ValueError):
            logarithm(-5, 2)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(6, 8), 10)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)

    def test_sqrt(self):  # 3 assertions
        # Test basic function
        self.assertAlmostEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(16), 4)
        # Test for invalid argument
        with self.assertRaises(ValueError):
            square_root(-1)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()

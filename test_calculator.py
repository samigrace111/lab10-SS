# https://github.com/samigrace111/lab10-SS
# Partner 1: Samantha Sobrino
# Partner 2:

import unittest
from calculator import (
    add, subtract, multiply, divide, 
    mul, div, logarithm, exp, hypotenuse, square_root
)

class TestCalculator(unittest.TestCase):
 
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-2, -2), 0)
        self.assertEqual(subtract(10, 20), -10)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)
        self.assertEqual(multiply(-3, 5), -15)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(5, 0), "Error: Cannot divide by zero")
        
    def test_mul(self):
        self.assertEqual(mul(3, 3), 9)
        self.assertEqual(mul(-1, 5), -5)
        self.assertEqual(mul(0, 9), 0)

    def test_div(self):
        self.assertEqual(div(8, 2), 4)
        self.assertEqual(div(-10, 2), -5)
        self.assertEqual(div(5, 0), "Error: Cannot divide by zero")

    def test_logarithm_valid(self):
        # log base 2 of 8 is 3
        self.assertAlmostEqual(logarithm(8, 2), 3)
        # log base 5 of 25 is 2
        self.assertAlmostEqual(logarithm(25, 5), 2)
        # log base 10 of 10 is 1
        self.assertAlmostEqual(logarithm(10, 10), 1)

    def test_logarithm_invalid_base(self):
        # base 0 or base == 1 or negative base not allowed
        with self.assertRaises(ValueError):
            logarithm(8, 1)
        with self.assertRaises(ValueError):
            logarithm(8, 0)
        with self.assertRaises(ValueError):
            logarithm(8, -2)

    def test_logarithm_invalid_argument(self):
        # negative argument or zero not allowed
        with self.assertRaises(ValueError):
            logarithm(-5, 2)
        with self.assertRaises(ValueError):
            logarithm(0, 2)

    def test_exp(self):
        self.assertEqual(exp(2, 3), 8)
        self.assertEqual(exp(-2, 3), -8)
        self.assertEqual(exp(10, 0), 1)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(6, 8), 10)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)

    def test_square_root_valid(self):
        self.assertAlmostEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(16), 4)
        self.assertAlmostEqual(square_root(0), 0)

    def test_square_root_invalid(self):
        with self.assertRaises(ValueError):
            square_root(-1)

if __name__ == '__main__':
    unittest.main()

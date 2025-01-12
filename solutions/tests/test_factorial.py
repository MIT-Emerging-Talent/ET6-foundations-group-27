"""
Unit tests for factorial_calculator.py.
"""

import unittest

from solutions.factorial import factorial


class TestSolutionFactorial(unittest.TestCase):
    """
    Unit tests for the factorial function.
    """

    def test_factorial_zero(self):
        """
        Test factorial of 0 is 1.
        """
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        """
        Test factorial of 1 is 1.
        """
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive(self):
        """
        Test factorial of a positive integer.
        """
        self.assertEqual(factorial(5), 120)

    def test_large_factorial(self):
        """
        Test factorial of a larger number.
        """
        self.assertEqual(factorial(10), 3628800)

    def test_negative_input(self):
        """
        Test that negative inputs raise a ValueError.
        """
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_non_integer_input(self):
        """
        Test that non-integer inputs raise a TypeError.
        """
        with self.assertRaises(TypeError):
            factorial(5.5)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""unit tests for the factorial function in the factorial calculator module"""

# Ayham
import unittest

from ..factorial_calculator import factorial


class TestFactorial(unittest.TestCase):
    """
    testing the factorial function. (edge cases and invalid inputs)
    """

    def test_factorial_positive(self):
        """It should return the factorial of positive integers."""
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        """it should return the factorial of zero > 1"""
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        """it should raise VAlueError for negative integers input"""
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_factorial_none(self):
        """It should raise a ValueError for None as an input"""
        with self.assertRaises(ValueError):
            factorial(None)

    def test_factorial_non_integer(self):
        """It should raise TypeError when passing non integer values"""
        with self.assertRaises(TypeError):
            factorial(3.5)

    def test_factorial_large_numbers(self):
        """ensuring it would compute the factorial for large inputs"""
        self.assertEqual(factorial(14), 87178291200)


if __name__ == "__main__":
    unittest.main()

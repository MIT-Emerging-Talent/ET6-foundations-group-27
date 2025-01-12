#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unit tests for the summation function
"""

import unittest

from solutions.summation import sum

"""tests for the sum function"""


class TestSum(unittest.TestCase):
    """It should return the sum of positive numbers"""

    def test_sum_positive_numbers(self):
        actual = sum(1, 2, 3, 4, 5)  # noqa: F841
        expected = 15  # noqa: F841
        self.assertEqual(actual, expected)  # noqa: F821

    """It should return the sum of a negative numbers"""

    def test_sum_negative_numbers(self):
        actual = sum(-1, -2, -3, -5)  # noqa: F841
        expected = -11
        self.assertEqual(actual, expected)

    """It should return the sum of a mix numbers"""

    def test_sum_mixed_numbers(self):
        actual = sum(10, -20, -40, 50)
        expected = 0
        self.assertEqual(actual, expected)

    """It should return the sum of a float numbers"""

    def test_sum_float_numbers(self):
        actual = sum(1.5, 2.5, 3.7, 4.5)
        expected = 12.2
        self.assertEqual(actual, expected)

    """It should return the sum of zero numbers"""

    def test_sum_zero_numbers(self):
        actual = sum(0, 0, 0, 0)
        expected = 0
        self.assertEqual(actual, expected)

    """It should return the single argument when only one is provided."""

    def test_sum_single_argument(self):
        actual = sum(10)
        expected = 10
        self.assertEqual(actual, expected)

    """It should return 0 when no arguments are provided."""

    def test_sum_no_arguments(self):
        actual = sum()
        expected = 0
        self.assertEqual(actual, expected)

    """It should raise a TypeError for string input."""

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            sum(1, 2, "string", 4)

    """It should raise a TypeError for None as an input."""

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            sum(1, None, 3)

    """It should raise a TypeError for mixed valid and invalid inputs."""

    def test_invalid_input_mixed(self):
        with self.assertRaises(TypeError):
            sum(10, 5, "invalid", 2)

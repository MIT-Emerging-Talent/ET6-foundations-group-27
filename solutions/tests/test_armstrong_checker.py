#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the armstrong_checker module.
"""

import unittest

from ..armstrong_checker import armstrong_checker


class TestArmstrongChecker(unittest.TestCase):
    """Test cases for the armstrong_checker function."""

    def test_valid_armstrong_numbers(self):
        """Test cases where the number is an Armstrong number."""
        self.assertEqual(armstrong_checker(153), "True")

    def test_non_armstrong_numbers(self):
        """Test cases where the number is not an Armstrong number."""
        self.assertEqual(armstrong_checker(123), "False")

    def test_invalid_input_negative_number(self):
        """Test case for a negative number input."""
        with self.assertRaises(ValueError):
            armstrong_checker(-153)

    def test_invalid_input_string(self):
        """Test case for a string input."""
        with self.assertRaises(ValueError):
            armstrong_checker("153")

    def test_invalid_input_float(self):
        """Test case for a float input."""
        with self.assertRaises(ValueError):
            armstrong_checker(0.5)

    def test_armstrong_number_single_digit(self):
        """Test a single-digit Armstrong number."""
        self.assertEqual(armstrong_checker(5), "True")

    def test_invalid_input_zero(self):
        """Test zero as input (invalid)."""
        with self.assertRaises(ValueError):
            armstrong_checker(0)

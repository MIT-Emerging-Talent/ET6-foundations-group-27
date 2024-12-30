"""
Test module for quadratic_sequence function.

Test categories:
    - Standard cases: The input is a list of integers.
    - Edge cases: The input is equal to 0 or 1.
    - Defensive cases: wrong input types, assertions

Created on 2024-12-30
Author: Omnia Mustafa - Abdulgadir
"""

import unittest

from ..quadratic_sequence import quadratic_sequence


class TestQuadraticSequence(unittest.TestCase):
    # Edge cases:
    def test_all_inputs_are_0(self):
        """Test case when all inputs equal to 0"""
        self.assertEqual(quadratic_sequence(0, 0, 0, 0), [])

    def test_n_is_0(self):
        """Test case when n is equal to 0"""
        self.assertEqual(quadratic_sequence(5, 3, 2, 0), [])

    def test_all_inputs_are_1(self):
        """Test case when all inputs equal to 1"""
        self.assertEqual(quadratic_sequence(1, 1, 1, 1), [3])

    def test_a_is_0(self):
        """Test case when a is equal to 0"""
        self.assertEqual(quadratic_sequence(0, 5, 3, 2), [8, 13])

    def test_b_is_0(self):
        """Test case when b is equal to 0"""
        self.assertEqual(quadratic_sequence(5, 0, 3, 2), [8, 23])

    def test_c_is_0(self):
        """Test case when c is equal to 0"""
        self.assertEqual(quadratic_sequence(5, 3, 0, 2), [8, 26])

    # Standard cases:
    def test_equal_inputs(self):
        """Test case when all inputs are equal"""
        self.assertEqual(quadratic_sequence(3, 3, 3, 3), [9, 21, 39])

    def test_different_inputs(self):
        """Test case when all inputs are different"""
        self.assertEqual(quadratic_sequence(1, 2, 3, 4), [6, 11, 18, 27])

    # Defensive cases:
    def wrong_input_a_type(self):
        """Test when input a is not integer"""
        with self.assertRaises(AssertionError):
            quadratic_sequence("1", 1, 1, 1)

    def wrong_input_b_type(self):
        """Test when input b is not integer"""
        with self.assertRaises(AssertionError):
            quadratic_sequence(5, "Omnia", 10, 6)

    def wrong_input_c_type(self):
        """Test when input c is not integer"""
        with self.assertRaises(AssertionError):
            quadratic_sequence(1, 5, [1, 2, 3], 8)

    def wrong_input_n_type(self):
        """Test when input n is not integer"""
        with self.assertRaises(AssertionError):
            quadratic_sequence(1, 1, 5, [1, 2, 3])

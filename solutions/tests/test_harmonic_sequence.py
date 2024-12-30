"""
Test module for harmonic_sequence function.

Test categories:
    - Standard cases: The input is a list of integers.
    - Edge cases: The input is equal to 0 or 1.
    - Defensive cases: wrong input types, assertions

Created on 2024-12-30
Author: Omnia Mustafa - Abdulgadir
"""

import unittest

from ..harmonic_sequence import harmonic_sequence


class TestHarmonicSequence(unittest.TestCase):
    """
    This class, `TestHarmonicSequence`, contains a set of test cases for the `harmonic_sequence` function. The test cases cover various scenarios, including edge cases, standard cases, and defensive cases.

        The edge cases include:
            - When all inputs are equal to 1
            - When `n` is equal to 0
            - When `a` and `d` are equal to 0
            - When `n` is negative
            - When `a` and `d` are equal to 1

        The standard cases include:
            - When all inputs are integers and greater than 1
            - When `n` is large

        The defensive cases include:
            - When the input `a` is not an integer
            - When the input `d` is not an integer
            - When the input `n` is not an integer

    These test cases ensure that the `harmonic_sequence` function
    behaves as expected under various input conditions.
    """

    # Edge cases:
    def test_min_input1(self):
        """Test case when all inputs equal to 1"""
        self.assertEqual(harmonic_sequence(1, 1, 1), [1.0])

    def test_n_equal_0(self):
        """Test case when n is equal to 0"""
        self.assertEqual(harmonic_sequence(1, 1, 0), [])

    def test_a_and_d_equal_0(self):
        """Test case when a and d are equal to 0"""
        self.assertEqual(harmonic_sequence(0, 0, 5), [0, 0, 0, 0, 0])

    def test_n_negative(self):
        """Test case when n is negative"""
        self.assertEqual(harmonic_sequence(1, 1, -1), [])

    def test_a_and_d_equal_1(self):
        """Test a and d are equal 1"""
        self.assertEqual(
            harmonic_sequence(1, 1, 5), [1.0, 0.5, 0.3333333333333333, 0.25, 0.2]
        )

    # Standard cases:
    def test_all_inputs_greater_than_1(self):
        """Test when all inputs are integer and greater than 1"""
        self.assertEqual(harmonic_sequence(2, 2, 3), [0.5, 0.25, 0.16666666666666666])

    def test_n_is_large(self):
        """Test when n is large"""
        self.assertEqual(
            harmonic_sequence(4, 3, 10),
            [
                0.25,
                0.14285714285714285,
                0.1,
                0.07692307692307693,
                0.0625,
                0.05263157894736842,
                0.045454545454545456,
                0.04,
                0.03571428571428571,
                0.03225806451612903,
            ],
        )

    # Defensive cases:
    def wrong_input_a_type(self):
        """Test when input a is not integer"""
        with self.assertRaises(AssertionError):
            harmonic_sequence("1", 1, 1)

    def wrong_input_d_type(self):
        """Test when input d is not integer"""
        with self.assertRaises(AssertionError):
            harmonic_sequence(5, "Omnia", 10)

    def wrong_input_n_type(self):
        """Test when input n is not integer"""
        with self.assertRaises(AssertionError):
            harmonic_sequence(1, 1, [1, 2, 3])

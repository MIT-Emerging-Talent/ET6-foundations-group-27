#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for robot function.

Test categories:
    - Standard cases
    - Edge cases
    - Defensive tests

Created on 2024-01-02
Author: Reem Osama
"""

import unittest
from ..robot import robot


class TestRobot(unittest.TestCase):
    """Test the robot function"""

    # Standard Cases
    def test_base_1x1(self):
        """A basic test with a small grid 1x1"""
        self.assertEqual(robot(1, 1), 1)

    def test_base_2x2(self):
        """A basic test with a small grid 2x2"""
        self.assertEqual(robot(2, 2), 2)

    def test_base_3x3(self):
        """A basic test with a small grid 3x3"""
        self.assertEqual(robot(3, 3), 6)

    def test_base_3x7(self):
        """A basic test with a small grid of 3x7"""
        self.assertEqual(robot(3, 7), 28)

    def test_base_4x3(self):
        """A basic test with a grid of 4x3"""
        self.assertEqual(robot(4, 3), 10)

    # Edge Cases
    def test_long_narrow(self):
        """A test for a long narrow grid of 1x10"""
        self.assertEqual(robot(1, 10), 1)

    def test_tall_narrow(self):
        """A test for a tall narrow grid 10x1"""
        self.assertEqual(robot(10, 1), 1)

    def test_large_grid(self):
        """A test for a moderately large grid 10x10"""
        self.assertEqual(robot(10, 10), 48620)

    def test_very_large_grid(self):
        """A test for a very large grid 20x15"""
        self.assertEqual(robot(20, 15), 818809200)

    # Defensive Cases
    def test_invalid_row(self):
        """A test for an invalid row input - not an integer"""
        with self.assertRaises(AssertionError):
            robot("3", 7)

    def test_invalid_col(self):
        """A test for an invalid column input - not an integer"""
        with self.assertRaises(AssertionError):
            robot(3, "7")

    def test_negative_value(self):
        """A test with a negative dimension"""
        with self.assertRaises(ValueError):
            robot(-1, 5)

    def test_zero_value(self):
        """A test with zero value"""
        with self.assertRaises(ValueError):
            robot(3, 0)

    def test_non_integer_input(self):
        """A test wit a non integer input for both dimensions"""
        with self.assertRaises(AssertionError):
            robot(2.5, 3.7)

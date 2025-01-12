#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test_draw_triangle.py

this module contains unit tests for the 'draw_triangle' function.

"""

import unittest
from io import StringIO
import sys
from ..draw_triangle import draw_triangle


class TestDrawTriangle(unittest.TestCase):
    """test the draw triangle function"""

    def setUp(self):
        """set up for capturing printed output"""
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        """reset standard output"""
        sys.stdout = sys.__stdout__

    def test_valid_input(self):
        """test the function with valid input"""
        draw_triangle(4)
        self.assertEqual(self.captured_output.getvalue(), "****\n***\n**\n*\n")

    def test_large_input(self):
        """test the function with a large input"""
        draw_triangle(7)
        self.assertEqual(
            self.captured_output.getvalue(),
            "*******\n******\n*****\n****\n***\n**\n*\n",
        )

    def test_non_integer_input(self):
        """test the function with a non integer input"""
        with self.assertRaises(AssertionError):
            draw_triangle("aa")

    def test_negative_input(self):
        """test the function with a negative input"""
        with self.assertRaises(ValueError):
            draw_triangle(-3)

    def test_zero_input(self):
        """test the function with zero as the input"""
        with self.assertRaises(ValueError):
            draw_triangle(0)

    def test_small_input(self):
        """test the function with the smallest input"""
        draw_triangle(1)
        self.assertEqual(self.captured_output.getvalue(), "*\n")

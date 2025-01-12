#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for Roman to integer function.

Author: Safia Gibril
Created on: 2.1.2025
"""

import unittest

from solutions.Roman_to_integer import RomanConverter


class TestRomanToInteger(unittest.TestCase):
    """
    Unittest class to test the roman_to_integer function.
    """

    def test_case_0(self):
        """Test conversion of single Roman (X) to numeral 10"""
        self.assertEqual(RomanConverter().roman_to_integer("X"), 10)

    def test_case_1(self):
        """Test conversion of Roman numeral to 1000 (M)"""
        self.assertEqual(RomanConverter().roman_to_integer("M"), 1000)

    def test_case_2(self):
        """Test conversion of Roman (XC) to numeral 90"""
        self.assertEqual(RomanConverter().roman_to_integer("XC"), 90)

    def test_case_3(self):
        """Test conversion of Roman (IX) numeral to 9"""
        self.assertEqual(RomanConverter().roman_to_integer("IX"), 9)

    def test_case_4(self):
        """Test conversion of Roman (LXXXVII) numeral to 87"""
        self.assertEqual(RomanConverter().roman_to_integer("LXXXVII"), 87)

    def test_case_5(self):
        """Test conversion of Roman numeral to 3999 (MMMCMXCIX)"""
        self.assertEqual(RomanConverter().roman_to_integer("MMMCMXCIX"), 3999)

    def test_case_6(self):
        """Test non-string input, expect 0"""
        self.assertEqual(RomanConverter().roman_to_integer(123), 0)

    def test_case_7(self):
        """Test non-string input (None), expect 0"""
        self.assertEqual(RomanConverter().roman_to_integer(None), 0)

    def test_case_8(self):
        """Test empty string input, expect 0"""
        self.assertEqual(RomanConverter().roman_to_integer(""), 0)

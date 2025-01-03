#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for is_anagram function.

Test categories:
    - Standard cases: typical string lists
    - Edge cases: empty strings, equal lengths
    - Defensive tests: invalid inputs

Created on 2024-01-02
Author: Reem Osama
"""

import unittest

from ..is_anagram import is_anagram


class TestIsAnagram(unittest.TestCase):
    """Test suite for the is_anagram function"""

    # Standard Cases:
    def test_base_one(self):
        """A basic test for valid cases"""
        self.assertEqual(is_anagram("listen", "silent"), True)

    def test_different_length(self):
        """A test for string with unequal lengths"""
        self.assertEqual(is_anagram("apple", "apples"), False)

    # Edge Cases:
    def test_case_sensitivity(self):
        """A test for case sensitivity strings"""
        self.assertEqual(is_anagram("Listen", "silent"), False)

    def test_white_space(self):
        """A test for whitespace handling"""
        self.assertEqual(is_anagram("dormitory", "dirty room"), False)

    def test_space_in_middle(self):
        """A test for handling spaces in the middle of two strings"""
        self.assertEqual(is_anagram("the eyes", "they see"), True)

    def test_special_characters(self):
        """A test with inputs with punctuation or non-alphabetic chars"""
        self.assertEqual(is_anagram("a+b=c", "c+b=a"), True)

    def test_empty_strings(self):
        """A test with empty strings"""
        self.assertEqual(is_anagram("", ""), True)

    def test_single_characters(self):
        """A test with single character strings"""
        self.assertEqual(is_anagram("a", "b"), False)

    def test_numerical_strings(self):
        """A test with numerical strings"""
        self.assertEqual(is_anagram("123", "321"), True)

    def test_large_inputs(self):
        """A test with large strings"""
        large_str1 = "a" * 10000 + "b" * 10000
        large_str2 = "b" * 10000 + "a" * 10000
        self.assertEqual(is_anagram(large_str1, large_str2), True)

    # Defensive tests:
    def test_invalid_input(self):
        """A test with invalid input"""
        with self.assertRaises(AssertionError):
            is_anagram(123, "abc")


if __name__ == "__main__":
    unittest.main()

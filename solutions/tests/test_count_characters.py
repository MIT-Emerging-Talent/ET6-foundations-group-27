#!/usr/bin/env python3
# -- coding: utf-8 --
"""
test_count_characters.py
this module contains unit tests for the 'count_characters'
function

"""

import unittest

from ..count_characters import count_characters


class TestCountCharacters(unittest.TestCase):
    # Edge cases:
    def test_empty_string(self):
        """check if the input is empty string"""
        self.assertEqual(count_characters(""), 0)

    def test_no_vowels(self):
        """check if string has no vowels"""
        self.assertEqual(count_characters("krm"), 0)

        """check if string is just whitespace"""
        self.assertEqual(count_characters(" "), 0)

    # Standard cases:
    def test_lowercase_word(self):
        """check if handles lowercase correctly"""
        self.assertEqual(count_characters("hello"), 2)

    def test_uppercase_word(self):
        """check if handles uppercase correctly"""
        self.assertEqual(count_characters("RAFF"), 1)

    def test_mixed_case(self):
        """check if handles mixed case correctly"""
        self.assertEqual(count_characters("aEiOu"), 5)

    def test_sentence(self):
        """check if handles full sentence correctly"""
        self.assertEqual(count_characters("Hello World"), 3)

    def test_all_vowels(self):
        """check if counts all vowel types correctly"""
        self.assertEqual(count_characters("AeIoU"), 5)

    # defensive cases
    def test_number_input(self):
        """It should raise AssertionError for integer input"""
        with self.assertRaises(AssertionError):
            count_characters(123)

    def test_list_input(self):
        """It should raise AssertionError for list input"""
        with self.assertRaises(AssertionError):
            count_characters(["hello"])

    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            count_characters(None)

    def test_float_input(self):
        """It should raise AssertionError for float input"""
        with self.assertRaises(AssertionError):
            count_characters(3.14)

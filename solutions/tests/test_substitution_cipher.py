#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the cipher function
"""

import unittest

from solutions.substitution_cipher import cipher


class TestSubstitutionCipher(unittest.TestCase):
    """
    testing cipher function
    """

    def test_lowercase(self):
        """
        testing lower case encryption
        """
        self.assertEqual(cipher("abc"), "def")

    def test_mixed_cases(self):
        """
        testing lower and upper case mixed letters
        """
        self.assertEqual(cipher("AbCd"), "DeFg")

    def test_edge_cases(self):
        """
        testing edge cases such as reaching the end of the alphabets
        """
        self.assertEqual(cipher("xyz"), "abc")

    def test_invalid_chars(self):
        """
        testing that ivalid chars remain unchanged when mixed with alphabets
        """
        self.assertEqual(cipher("Hello@123!"), "Khoor@123!")


if __name__ == "__main__":
    unittest.main()

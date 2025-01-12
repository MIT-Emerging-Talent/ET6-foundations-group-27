#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for converting Roman numerals to integers.

Provides the RomanConverter class with a method to convert valid Roman numeral strings
into their integer representation.

Author: Safia Gibril
Created on: 2.1.2025
"""


class RomanConverter:
    """This class identify Roman Converter."""

    def roman_to_integer(self, roman_str: str) -> int:
        """
        Convert a Roman numeral string to an integer.

        Args:
            roman_str (str): The Roman numeral string to convert.

        Returns:
            int: The integer representation of the Roman numeral.

        Exceptions:
            If `roman_str` is not a string or is None, return 0.


        """
        if not isinstance(roman_str, str) or roman_str is None:
            return 0

        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0

        for idx, char in enumerate(roman_str):
            if idx + 1 < len(roman_str) and roman[char] < roman[roman_str[idx + 1]]:
                result -= roman[char]
            else:
                result += roman[char]

        return result

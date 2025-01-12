#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Creates a function that counts the number of vowels (a, e, i, o, u) in a given string.
The function is case-insensitive, meaning both uppercase and lowercase vowels are counted.

Author: Rafaa Ali
Created date: 3.1.2025
"""


def count_characters(string: str) -> int:
    """This function, `count_vowels`, counts the number of vowels in a given string,
    ignoring case sensitivity.

    Parameters:
    string (str): The input string to count vowels characters

    Returns:
    int: The total number of vowels in the string

    assertion:
    string must be string type otherwise error

    example:
    Edge cases:
    >>> count_characters("")
    0
    >>> count_characters("krm")
    0
    >>> count_characters(" ")
    0

    Standard cases:
    >>> count_characters lowercase("hello")
    2
    >>> count_characters uppercase("RAFF")
    1
    >>>count_characters mixed case("aEiOu")
    5

    Defensive cases:
    >>> count_characters(123)
    AssertionError: Input must be string
    >>>count_characters(["hello"])
    AssertionError: Input must be string
    >>> count_characters(None)
    AssertionError: Input must be string
    """
    # assert an error when input is not string
    assert isinstance(string, str), "Input must be string"

    # Convert string to lowercase for case-insensitive counting
    string = string.lower()

    # Define vowels to check against
    vowels = "aeiou"

    # Initialize counter for vowels
    count = 0

    # Loop through each character in the string
    for char in string:
        # If character is a vowel, increment counter
        if char in vowels:
            count += 1

    # Return the total count of vowels
    return count

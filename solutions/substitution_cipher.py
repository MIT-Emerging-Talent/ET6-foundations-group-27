#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Substitution Cipher
this code provides a function to encrypt text using a caesar cipher,
shifting lower and uppercase letter by a fixed value of 3 (as per the challenge)
"""

# Author: AYHAM, 1/1/2025

import string


def cipher(text: str) -> str:
    """
    Parameters:
        text (str): The text to be encrypted.
        Assumes input consists of alphabetic chars, optionally mixed with non alphabetic chars
        those would remain unchanged.


    Returns:
        str: The encrypted text. only alphabetic characters shifted by 3 positions
        and non alphabetical values unchanged.

    Raises:
    ValueError: If input is not a string

        >>> cipher("abc")
        'def'
        >>> cipher("omnia")
        'rpqld'
        >>> cipher("Hello!")
        'Khoor!'

    """

    shift_value = 3

    # Validate that the input is a string.
    if not isinstance(text, str):
        raise ValueError("Input text must be a string.")

    # Define lowercase and uppercase alphabets for shifting.
    alphabets = [string.ascii_lowercase, string.ascii_uppercase]

    def shift_alphabet(alphabet: str) -> str:
        return alphabet[shift_value:] + alphabet[:shift_value]

    # Generate shifted versions of the alphabets.
    shifted_alphabets = tuple(map(shift_alphabet, alphabets))

    # Combine original and shifted alphabets into strings for translation.
    final_alphabet = "".join(alphabets)
    final_shifted_alphabet = "".join(shifted_alphabets)

    # Create a translation table to map characters to their shifted counterparts.
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

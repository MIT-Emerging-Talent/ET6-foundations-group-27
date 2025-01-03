#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function that takes two strings as input and checks if they
are anagrams of each other. Anagrams are words or phrases made by
rearranging the letters of another, using all original letters
exactly once

True if the two strings are anagrams, False otherwise

"""

from collections import Counter


def is_anagram(first_word: str, second_word: str) -> bool:
    """
    Returns true or false if the two strings given are anagrams
    of each other.

    Anagram is word or a phrase formed by rearranging the letters of another
    word or phrase, using all the original letters exactly once

    "listen" -> "silent"

    Parameters:
        first_word: The first string
        second_word: The second string

    Returns -> bool: Either true or false of either the strings
    are anagrams of each other or not.

    Raises:
        AssertionError: if the parameters are not strings

    Examples:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("rat", "car")
        False
        >>> is_anagram("evil", "vile")
        True
    """
    assert isinstance(first_word, str), "First word must be a string"
    assert isinstance(second_word, str), "Second word must be a string"

    if len(first_word) != len(second_word):
        return False

    # This is a time complexity of O(n log n) answer
    # return sorted(first_word) == sorted(second_word)

    # This is a time complexity of O(n) answer
    return Counter(first_word) == Counter(second_word)

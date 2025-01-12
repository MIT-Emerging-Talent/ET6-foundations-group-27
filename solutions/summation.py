#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for determining whether a given number is a sum of a defined number.

Module contents:
    - sum: checks if a given integer is a sum of those given numbers.

Created on 01/01/2025

@author: Safa Ishag

Challenge is from the Leetcode website.

Defining the sum of a given number:

"""


def sum(*args: float) -> float:
    """
    Return the sum of all input numbers.

    Parameters:
        *args (int or float): The number to check and is the variable.

    Returns:
    int or float: The sum of all input numbers.

    Raises:
        TypeError: If any input is not a number.

    Example:
    >>> sum(1, 2, 3, 4, 5)
    15
    >>> sum(3, 6, 2, 1, 8)
    20
    >>> sum(4, 9, 7, 2, 5)
    27

    """
    # Defensive assertion: Ensure all inputs are numbers
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("All inputs must be numeric (int or float).")

        # Iterate through the input arguments and calculate the sum

    total = 0

    for i in args:
        total += i

    return total

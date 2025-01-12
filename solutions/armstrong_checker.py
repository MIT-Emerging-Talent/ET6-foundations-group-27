#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module checks if a number is an Armstrong number.
Created on 2025-01-02
Author: Ahmed
"""


def armstrong_checker(number: int) -> str:
    """
    Checks if a given positive integer is an Armstrong number.

    Parameters:
        number (int): The number to check (must be > 0).

    Returns:
        str:
            - "True" if the number is an Armstrong number.
            - "False" if the number is not an Armstrong number.

    Raises:
        ValueError: If the input is not a positive integer.

    Examples:
        >>> armstrong_checker(153)
        'True'
        >>> armstrong_checker(123)
        'False'
        >>> armstrong_checker(9474)
        'True'
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Invalid input: number must be a positive integer.")

    # Calculate the sum of the nth power of each digit in the number.
    digits = [int(d) for d in str(number)]
    n = len(digits)
    armstrong_sum = sum(d**n for d in digits)

    return "True" if armstrong_sum == number else "False"
    # if the sum of the nth power of each digit in the number
    # is equal to the number, return "True", otherwise return "False"

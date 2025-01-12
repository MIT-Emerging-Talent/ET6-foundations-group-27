#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
factorial calculator,
This module provides a function to calculate the factorial of a given non-negative integer.

Mathematical Definition:
n! = n * (n - 1) * (n - 2) * ... * 1

By convention, 0! = 1.

"""
# Author: AYHAM
# Date: 6/jan/2025


def factorial(n: int) -> int:
    """
    Parameters:
    n(int): The number to calculate the factorial of. it should be a positive integer only

    Returns:
    int: the factorial of the given number

    Raises:
    ValueError -> If the input is None or a Negative integer
    TypeError -> if the input is not an integer

    Examples:

    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(3)
    6

    """

    if n is None:
        raise ValueError("Input cannot be None")

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    # initialize the result variable
    fact = 1
    # a loop to compute the factorial
    for i in range(1, n + 1):
        fact *= i
    return fact

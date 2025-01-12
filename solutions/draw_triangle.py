#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
module'draw': it prints a triangle pattern made of stars (*).

the user enters a number and get a triangle of stars in descending order.

Author: Mohamed Tilal
Created date: 6.1.2025
"""
# the function


def draw_triangle(n: int) -> None:
    """
    Prints a descending triangle pattern of stars (*).


    parameters:
        n (int): The number of stars in the first row.
        Must be a positive integer.

    Returns:
        None: The function prints the pattern but does not return any value.


    Raises:
        assertionError: if 'n' is not an integer
        assertionError: if 'n' is less than one


    Examples:
    >>> draw_triangle(5)
      *****
      ****
      ***
      **
      *

    >>> draw_triangle(3)
        ***
        **
        *

    """

    assert isinstance(n, int), " parameter 'n' must be an integer"

    if n < 1:
        raise ValueError("parameter 'n' must be greater than or equal to 1.")

    for a in range(n, 0, -1):
        """ creates a sequence from n down to 1"""
        print("*" * a)

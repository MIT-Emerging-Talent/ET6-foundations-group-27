#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating a sequence for arithmetic numbers

Module contents:
    -arithmetic_sequence:generating a sequence of n arithmetic numbers.

Created on Sunday 22/December/2024
@author: Mayar Ali
"""

# ---before documenting and testing---


def arithmetic_sequence(sequence_length: int) -> list:
    """
         Return a list in which the difference between,
           consecutive terms are constant.


        Parameters:
        sequence_length:int, greater than zero

    Returns -list[int] with the first n number of the arithmetic sequence

    Raises:
        AssertionError : if the argument is not an integer
        AssertionError : if the argument is less or equal to zero

        Examples:
        >>>arithmetic_sequence(0)
        [1]
        >>>arithmetic_sequence(5)
        [0 ,1 ,5 ,9 ,13]
        >>>arithmetic_sequence(11)
        [0 ,1 ,5 ,9 ,13 ,17 ,21 ,25 ,29 ,33 ,37 ]
    """
    assert isinstance(sequence_length, int)
    assert sequence_length >= 0

    if sequence_length == 0:
        return []
    if sequence_length == 1:
        return [0]
    if sequence_length == 2:
        return [0, 1]
    sequence = [0, 1]
    while len(sequence) < sequence_length:
        sequence.append(sequence[-1] + 3)

    return sequence

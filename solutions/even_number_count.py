#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A function that counts the number of even numbers in a countdown from n to 1

Module contents:
    - even_number_count: gen number for even numbers in the list.

Created on Monday/ 30/ December/ 2024
@author: Mayar Ali.
"""


def even_number_count(number: list) -> int:
    """Returns the number of even numbers on the list.

    Parameters:
    int: list, the input list to process

    return - > int:  indicating the number of even number in the list

    Raises:
        AssertionError:

    Examples:
        >>> even_number_count ([1])
        0
        >>> even_number_count ([2,1])
        1
        >>> even_number_count ([3,2,1])
        1
    """
    assert isinstance(number, list)
    for num in number:
        assert isinstance(num, int)
    count = 0

    for num in number:
        if num % 2 == 0:
            count += 1
    return count


if __name__ == "__main__":
    print(even_number_count([1, 2, 3, 4, 5]))

#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Creates a sequence where numbers divisible by 4 return 'Foo',
numbers divisible by 6 return 'Bar', numbers divisible by both
return 'FooBar', and other numbers remain unchanged.

Author: Rafaa Ali
Created date: 1.1.2025
"""


def FooBar_code(n: int):
    """This function, FooBar_code, creates a sequence that replaces numbers
    based on their divisibility by 4 and 6.

    Parameters:
    n (int): The last number in the list.

    Returns:
    List: A list containing the sequence with 'Foo', 'Bar', 'FooBar' or numbers.

    Assertions:
    n must be an integer; otherwise, an error will be raised.

    Example:
    >>> FooBar_code(1)
    [1]
    >>> FooBar_code(0)
    []
    >>> FooBar_code(-1)
    []

    Standard cases:
    >>> FooBar_code(8)
    [1, 2, 3, 'Foo', 5, 'Bar', 7, 'Foo']
    >>> FooBar_code(12)
    [1, 2, 3, 'Foo', 5, 'Bar', 7, 'Foo', 9, 10, 11, 'FooBar']
    >>> FooBar_code(16)
    [1, 2, 3, 'Foo', 5, 'Bar', 7, 'Foo', 9, 10, 11, 'FooBar', 13, 14, 15, 'Foo']

    Defensive cases:
    >>> FooBar_code("rafaa")
    AssertionError: n must be an integer
    >>> FooBar_code(5.5)
    AssertionError: n must be an integer
    >>> FooBar_code([1, 2, 3])
    AssertionError: n must be an integer
    """
    # Assert an error when n is not an integer
    assert isinstance(n, int), "n must be an integer"
    if not isinstance:
        assert TypeError
    # Prepare an empty list for the result
    result = []

    # Loop for checking the sequence
    for i in range(1, n + 1):
        # Check if the number is divisible by both 4 and 6
        if i % 4 == 0 and i % 6 == 0:
            result.append("FooBar")
        # Check if the number is divisible by 4
        elif i % 4 == 0:
            result.append("Foo")
        # Check if the number is divisible by 6
        elif i % 6 == 0:
            result.append("Bar")
        # Otherwise, add the number to the list
        else:
            result.append(i)

    # Return the result's list
    return result

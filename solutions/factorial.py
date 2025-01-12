"""
This module provides a function to calculate the factorial of a number recursively.

The factorial function is defined only for non-negative integers.

Created on 01/01/2025

@author: Safa Ishag

Challenge is from the Leetcode website.

"""


def factorial(n: int) -> int:
    """
    Calculate the factorial of a given non-negative integer.

    Parameters:
        n (int): The number whose factorial is to be calculated. Must be >= 0.

    Returns:
        int: The factorial of the input number.

    Raises:
        ValueError: If `n` is negative.

    Doctests:
        >>> factorial(0)
        1
        >>> factorial(1)
        1
        >>> factorial(5)
        120
        >>> factorial(-1)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a non-negative integer.
    """
    # Defensive assertion: Input must be a non-negative integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

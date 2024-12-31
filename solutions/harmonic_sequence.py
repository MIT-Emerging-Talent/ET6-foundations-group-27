"""Creates harmonic sequence, based on formula: A(n): 1/ (a +(n-1) *d)
given a, d and n are integers. and returns
the list containing the harmonic sequence.

Created on 2024-12-30
Author: Omnia Mustafa - Abdulgadir
"""


def harmonic_sequence(a: int, d: int, n: int) -> list:
    """
    This function ,`harmonic_sequence`, creates a harmonic sequence,
    based on formula: A(n): 1/ (a +(n-1) *d)

    Parameters:
    a (int): First term
    d (int): Common difference
    n (int): Number of terms to generate

    Returns:
    List: List containing the harmonic sequence

    Assertions:
    - a must be integer
    - d must be integer
    - n must be integer

    Examples:
    Edge cases:
    >>> harmonic_sequence(1, 1, 1)
    [1.0]
    >>> harmonic_sequence(1, 1, 0)
    []
    >>> harmonic_sequence(0, 0, 5)
    [0, 0, 0, 0, 0]
    >>> harmonic_sequence(1, 1, -1)
    []
    >>> harmonic_sequence(1, 1, 5)
    [1.0, 0.5, 0.3333333333333333, 0.25, 0.2]

    Standard cases:
    >>> harmonic_sequence(2, 2, 3)
    [0.5, 0.25, 0.16666666666666666]
    >>> harmonic_sequence(4, 3, 10)
    [0.25,
        0.14285714285714285,
        0.1,
        0.07692307692307693,
        0.0625,
        0.05263157894736842,
        0.045454545454545456,
        0.04,
        0.03571428571428571,
        0.03225806451612903,]

    Defensive cases:
    >>> harmonic_sequence("1", 1, 1)
    AssertionError: A must be integer
    >>> harmonic_sequence(5, "Omnia", 10)
    AssertionError: D must be integer
    >>> harmonic_sequence(1, 1, [1, 2, 3])
    AssertionError: N must be integer
    """
    # Assert an error if any input is not integer
    assert isinstance(a, int), "A must be integer"
    assert isinstance(d, int), "D must be integer"
    assert isinstance(n, int), "N must be integer"

    # Create an empty list to save the sequence
    sequence = []
    # If n is less than or equal to 0, return empty list
    if n <= 0:
        return sequence
    # If a and d are equal to 0, return a list of n zeros
    if a == 0 and d == 0:
        return [0] * n
    # If all inputs are greater than 1, return the sequence
    for i in range(1, n + 1):
        term = 1 / (a + (i - 1) * d)
        sequence.append(term)
    return sequence

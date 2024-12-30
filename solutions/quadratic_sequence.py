def quadratic_sequence(a, b, c, n):
    """
    The function creates quadratic sequence, based on formula: A(n): a*n^2 + b*n + c

    Parameters:
    a (int): Coefficient of n^2
    b (int): Coefficient of n
    c (int): Constant term
    n (int): Number of terms to generate

    Returns:
    List: List containing the quadratic sequence

    Assertions:
    - a must be integer
    - b must be integer
    - c must be integer
    - n must be integer

    Examples:
    Edge cases:
    >>> quadratic_sequence(0, 0, 0, 0)
    []
    >>> quadratic_sequence(5, 3, 2, 0)
    []
    >>> quadratic_sequence(1, 1, 1, 1)
    [3]
    >>> quadratic_sequence(0, 5, 3, 2)
    [8, 13]
    >>> quadratic_sequence(5, 0, 3, 2)
    [8, 23]
    >>> quadratic_sequence(5, 3, 0, 2)
    [8, 26]
    Standard cases:
    >>> quadratic_sequence(3, 3, 3, 3)
    [9, 21, 39]
    >>> quadratic_sequence(1, 2, 3, 4)
    [6, 11, 18, 27]
    Defensive cases:
    >>> quadratic_sequence("1", 1, 1, 1)
    AssertionError: A must be integer
    >>> quadratic_sequence(5, "Omnia", 10, 6)
    AssertionError: B must be integer
    >>> quadratic_sequence(1, 5, [1, 2, 3], 8)
    AssertionError: C must be integer
    >>> quadratic_sequence(1, 1, 5, [1, 2, 3])
    AssertionError: N must be integer

    """
    # Assert error if inputs are not integers
    assert isinstance(a, int), "A must be integer"
    assert isinstance(b, int), "B must be integer"
    assert isinstance(c, int), "C must be integer"
    assert isinstance(n, int), "N must be integer"
    # Create quadratic sequence
    sequence = []
    # Return empty list if n is less than or equal to 0
    if n <= 0:
        return sequence
    # Create quadratic sequence
    for i in range(1, n + 1):
        term = (a * (i**2)) + (b * i) + c
        sequence.append(term)
    return sequence

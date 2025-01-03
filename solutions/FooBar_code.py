"""
Creates a sequence where numbers divisible by 4 return 'Foo',
numbers divisible by 6 return 'Bar', numbers divisible by both
return 'FooBar', and other numbers remain unchanged.

Author: Rafaa Ali
Created date: 1.1.2025
"""


def FooBar_code(n: int):
    """This function, `FooBar_code`, creates a sequence that replaces numbers
    based on their divisibility by 4 and 6.

    Parameters:
      n (int):the last number in the list

    Returns:
      List containing the sequence with 'Foo', 'Bar', 'FooBar' or numbers

    assertion:
    n must be integer otherwise error


    example:
    Edge cases:
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
    [1, 2, 3, 'Foo', 5, 'Bar', 7, 'Foo', 9, 10, 11, 'FooBar',
    13, 14, 15, 'Foo']

    Defensive cases:
    >>> FooBar_code("rafaa")
    AssertionError: N must be integer
    >>> FooBar_code(5.5)
    AssertionError: N must be integer
    >>> FooBar_code([1, 2, 3])
    AssertionError: N must be integer


    """
    # assert an error when n is not integer
    assert isinstance(n, int), "N must be integer"
    # prepare empty list for the result
    result = []
    # loop for checking the sequence
    for i in range(1, n + 1):
        #  checking if the number is devisable by 4 and 6
        if i % 4 == 0 and i % 6 == 0:
            # add FooBar to the list if it devisable by both 4,6
            result.append("FooBar")
        # checking if the number is devisable by 4
        elif i % 4 == 0:
            # add Foo to the list if it devisable by 4
            result.append("foo")
        # checking if the number is devisable by 6
        elif i % 6 == 0:
            # add Bar to the list if it devisable by 6
            result.append("Bar")
        # otherwise add the number to the list
        else:
            result.append(i)
    # return the result's list
    return result

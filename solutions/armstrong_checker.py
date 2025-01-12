"""Module checks if a number is an Armstrong number."""


def armstrong_checker(number: int) -> str:
    """
    Checks if a given positive integer is an Armstrong number.

    Parameters:
        number (int): The number to check (must be > 0).

    Returns:
        str:
            - "True" if the number is an Armstrong number.
            - "False" if the number is not an Armstrong number.
            - "Invalid input" for invalid inputs.

    Raises:
        AssertionError: If the input is not a positive integer.

    Examples:
        >>> armstrong_checker(153)
        'True'
        >>> armstrong_checker(123)
        'False'
        >>> armstrong_checker(-153)
        'Invalid input'
    """
    if not isinstance(number, int) or number < 0:
        return "Invalid input"

    # Calculate the sum of the nth power of each digit in the number.
    digits = [int(d) for d in str(number)]
    # digits puts each digit in the number into a list

    n = len(digits)
    # n is the number of digits in the number by using the len() function

    armstrong_sum = sum(d**n for d in digits)
    # armstrong_sum is the sum of the nth power of each digit in the number

    return "True" if armstrong_sum == number else "False"
    # if the sum of the nth power of each digit in the number
    # is equal to the number, return "True", otherwise return "False"

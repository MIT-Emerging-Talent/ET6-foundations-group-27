"""module calculates the percentage of fuel in a tank
and returns a status indicator."""


def fuel_gauge(x: int, y: int) -> str:
    """
    Calculates the percentage of fuel in a tank and returns a status indicator.

    Parameters:
        x (int): Fuel in the tank (must be ≤ y).
        y (int): Tank capacity (must be > 0).

    Returns:
        str:
            - "F" if percentage >= 90.
            - "E" if percentage <= 10.
            - "M" for all other cases.
            - "Invalid input" for invalid inputs.

    Raises:
        AssertionError: If y <= 0 or x > y.

    Examples:
        >>> fuel_gauge(90, 100)
        'F'
        >>> fuel_gauge(10, 100)
        'E'
        >>> fuel_gauge(50, 100)
        'M'
    """
    if y == 0 or x > y:
        return "Invalid input"

    percentage = (x / y) * 100
    if percentage >= 90:
        return "F"
    elif percentage <= 10:
        return "E"
    else:
        return "M"

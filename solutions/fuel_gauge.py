#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""module calculates the percentage of fuel in a tank and returns a status indicator.
Created on Sunday/29/December/2024
Author: Ahmed Elhassan"""


def fuel_gauge(fuel_amount: int, tank_capacity: int) -> str:
    """
    Calculates the percentage of fuel in a tank and returns a status indicator.

    Parameters:
        fuel_amount (int): Fuel in the tank (must be ≤ tank_capacity).
        tank_capacity (int): Tank capacity (must be > 0).

    Returns:
        str:
            - "F" if percentage >= 90.
            - "E" if percentage <= 10.
            - "M" for all other cases.
            - "Invalid input" for invalid inputs.

    Raises:
        AssertionError: If tank_capacity <= 0 or fuel_amount > tank_capacity.

    Examples:
        >>> fuel_gauge(90, 100)
        'F'
        >>> fuel_gauge(10, 100)
        'E'
        >>> fuel_gauge(50, 100)
        'M'
    """
    if tank_capacity <= 0 or fuel_amount > tank_capacity:
        raise AssertionError("Invalid tank capacity or fuel amount")

    percentage = (fuel_amount / tank_capacity) * 100

    if percentage >= 90:
        return "F"
    if percentage <= 10:
        return "E"
    return "M"

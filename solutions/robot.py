#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
There is a robot on an m x n grid. The robot is initially located
at the top-left corner (i.e., grid[0][0]). The robot tries to move
to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot
can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible
unique paths that the robot can take to reach the bottom-right
corner.

Constraints: The test cases are generated so that the answer will
be less than or equal to 2 * 109.
"""

def robot(m_: int, n_: int) -> int:
    """
    Returns the number of possible unique routes to reach the
    most bottom-right corner

    Parameters:
        m: The number of rows in the grid.
        n: The number of columns in the grid.

    Returns -> The number of unique paths from the top-left corner
    to the bottom-right corner.

    Raises:
        AssertionError: if m and n are not integers or less than 1

    Examples:
        >>> robot(3, 7)
        28
    """

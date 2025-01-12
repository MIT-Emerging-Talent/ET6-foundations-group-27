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

Created on 2024-01-01
Author: Reem Osama
"""


def robot_move(cell, rows, cols, memo) -> int:
    """
    This is a helper function that determines the number of unique paths by
    using dynamic programming and memoization

    Parameters:
        cell: a tuple made of two elements refers to the current location
        inside the grid - immutable, can be used as a key for dicts
        rows: The number of rows in the grid.
        cols: The number of columns in the grid.
        memo: a dictionary to save answers for memoization

    Returns -> The number of unique paths from the top-left corner
    to the bottom-right corner.
    """
    # if the cell is stored in the memo dict we return it
    if memo.get(cell):
        return memo.get(cell)
    # if the cell is directly perpendicular to target, there's only one road
    if cell[1] >= cols - 1 or cell[0] >= rows - 1:
        return 1
    # otherwise, there's two  roads to take, the answer is the sum of both
    memo[cell] = robot_move((cell[0] + 1, cell[1]), rows, cols, memo) + robot_move(
        (cell[0], cell[1] + 1), rows, cols, memo
    )
    # we save the answer in the memo for future referance and return it
    return memo[cell]


def robot(rows: int, cols: int) -> int:
    """
    Returns the number of possible unique routes to reach the
    most bottom-right corner

    Parameters:
        rows: The number of rows in the grid.
        cols: The number of columns in the grid.

    Returns -> The number of unique paths from the top-left corner
    to the bottom-right corner.

    Raises:
        AssertionError: if rows and cols are not integers or less than 1

    Examples:
        >>> robot(3, 7)
        28
        >>> robot(4, 3)
        10
        >>> robot(23, 12)
        193536720
    """
    # assert the values of rows and clos and make sure they are ints and
    # greater than 1
    assert isinstance(rows, int), "Rows variables has to be an integer"
    if rows <= 0:
        raise ValueError("The 'rows' variable must be greater than 0.")
    assert isinstance(cols, int), "Cols variable has to be an integer"
    if cols <= 0:
        raise ValueError("The 'cols' variables must be greater than 0.")

    # use the helper function robot_move to determine the number of paths
    memo = {}
    return robot_move((0, 0), rows, cols, memo)  # (0, 0) is the initial spot

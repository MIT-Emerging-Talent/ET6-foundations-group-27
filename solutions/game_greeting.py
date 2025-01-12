#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module: generate a game welcome message

the module provides a function that generates a welcome message for a player joining a game.

Author: Mohamed Tilal
Created date: 6.1.2025
"""
# the function:


def game_greeting(name: str) -> str:
    """
    the player inters his name as an input and in return he gets
    a greeting welcome massage.


    parameters:
      name (string)- The player's name. can be empty string or special characters.

    Returns:
      string- A formatted Welcome message in the form:
      "Welcome, [name] to the game"

    Raises:
      assertionError : if name is not a string

    Example:
      >>> game_greeting({Mohamed})
      "Welcome, Mohamed to the game"

    """
    assert isinstance(name, str), "Name should be string"

    return f"Welcome, {name} to the game"

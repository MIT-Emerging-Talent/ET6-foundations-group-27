#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test_game_greeting.py

this module contains unit tests for the 'game_greeting' function.
"""

import unittest

from ..game_greeting import game_greeting


class TestGameGreeting(unittest.TestCase):
    """test game greeting function"""

    def test_valid_name(self):
        """test the function with a valid name"""
        self.assertEqual(game_greeting("Mohamed"), "Welcome, Mohamed to the game")

    def test_empty_string(self):
        """test the function with an empty string"""
        self.assertEqual(game_greeting(""), "Welcome,  to the game")

    def test_special_characters(self):
        """test the function with special characters"""
        self.assertEqual(game_greeting("mx@z*"), "Welcome, mx@z* to the game")

    def test_integers(self):
        """test the function with integers"""
        with self.assertRaises(AssertionError):
            (game_greeting(573))

    def test_whitespace_name(self):
        """test the function with whitespace"""
        self.assertEqual(game_greeting("   "), "Welcome,     to the game")

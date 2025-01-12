#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Monday/30/December/2024
@author:Mayar Ali
"""

import unittest

# ---imports & test class before documenting and testing---
# from ..arithmetic_sequence import arithmetic_sequence
# class TestArithmeticSequence(unittest.TestCase):
# ---imports & test class after documenting and testing---

from ..arithmetic_sequence import arithmetic_sequence


class TestArithmeticSequence(unittest.TestCase):
    """Test the arithmetic_sequence function"""

    def test_empty_string(self):
        "It should evaluate 0 to []"
        self.assertEqual(arithmetic_sequence(0), [])

    def test_one_number(self):
        "Should evaluate 1 to [0]"
        self.assertEqual(arithmetic_sequence(1), [0])

    def test_two_numbers(self):
        "Should evaluate 2 to [0,1]"
        self.assertEqual(arithmetic_sequence(2), [0, 1])

    def test_three_numbers(self):
        "Should evaluate 3 to [0, 1, 5]"
        self.assertEqual(arithmetic_sequence(3), [0, 1, 4])

    # defensive cases

    def test_less_than_0(self):
        """It should raise an assertion error if the argument is less than 0"""
        with self.assertRaises(AssertionError):
            arithmetic_sequence(-1)

    def test_a_float(self):
        """Should raise an assertion error if the argument is a float"""
        with self.assertRaises(AssertionError):
            arithmetic_sequence(1.0)

    def test_a_string(self):
        """Should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            arithmetic_sequence(["1", 2, 3])

    # Edge case

    def test_a_big_number(self):
        "Should evaluate 100 to [0, 1, 5]"
        self.assertEqual(
            arithmetic_sequence(102),
            [
                0,
                1,
                4,
                7,
                10,
                13,
                16,
                19,
                22,
                25,
                28,
                31,
                34,
                37,
                40,
                43,
                46,
                49,
                52,
                55,
                58,
                61,
                64,
                67,
                70,
                73,
                76,
                79,
                82,
                85,
                88,
                91,
                94,
                97,
                100,
                103,
                106,
                109,
                112,
                115,
                118,
                121,
                124,
                127,
                130,
                133,
                136,
                139,
                142,
                145,
                148,
                151,
                154,
                157,
                160,
                163,
                166,
                169,
                172,
                175,
                178,
                181,
                184,
                187,
                190,
                193,
                196,
                199,
                202,
                205,
                208,
                211,
                214,
                217,
                220,
                223,
                226,
                229,
                232,
                235,
                238,
                241,
                244,
                247,
                250,
                253,
                256,
                259,
                262,
                265,
                268,
                271,
                274,
                277,
                280,
                283,
                286,
                289,
                292,
                295,
                298,
                301,
            ],
        )

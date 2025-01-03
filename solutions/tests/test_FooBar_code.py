import unittest

from ..FooBar_code import FooBar_code


class TestFooBar(unittest.TestCase):
    # Edge cases:
    def test_int1(self):
        """check if the input is 1"""
        self.assertEqual(FooBar_code(1), [1])

    def test_int0(self):
        """check if the input is 0"""
        self.assertEqual(FooBar_code(0), [])

    def test_negative_int(self):
        """check if the input is negative"""
        self.assertEqual(FooBar_code(-1), [])

    # Standard cases:
    def test_int8(self):
        """check if the input is 8"""
        self.assertEqual(FooBar_code(8), [1, 2, 3, "foo", 5, "Bar", 7, "foo"])

    def test_int12(self):
        """check if the input is 12"""
        self.assertEqual(
            FooBar_code(12), [1, 2, 3, "foo", 5, "Bar", 7, "foo", 9, 10, 11, "FooBar"]
        )

    def test_is_int(self):
        """check if the input is large number"""
        self.assertEqual(
            FooBar_code(16),
            [
                1,
                2,
                3,
                "foo",
                5,
                "Bar",
                7,
                "foo",
                9,
                10,
                11,
                "FooBar",
                13,
                14,
                15,
                "foo",
            ],
        )

    # defensive cases
    def test_string_input(self):
        """It should raise AssertionError for string input"""
        with self.assertRaises(AssertionError):
            FooBar_code("rafaa")

    def test_is_float_input(self):
        """It should raise AssertionError for float input"""
        with self.assertRaises(AssertionError):
            FooBar_code(5.5)

    def test_is_list_input(self):
        """It should raise AssertionError for list input"""
        with self.assertRaises(AssertionError):
            FooBar_code([1, 2, 3])

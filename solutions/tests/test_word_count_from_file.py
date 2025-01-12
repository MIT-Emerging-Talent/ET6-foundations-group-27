#!/user/bin/env python3
# *-* coding: utf-8 *-*
"""

Unit tests for the `word_count_txt_file` function.

Tests the following scenarios:
    - Correct word count for a file with a known number of words.
    - Handling of an empty file.
    - Word count for a file with multiple lines.
    - Assertion errors for non-existent files.
    - Assertion errors for non-.txt files.

"""

import unittest

from ..word_count_from_file import word_count_txt_file


class TestWordCountFromFile(unittest.TestCase):
    """Unit tests for the `word_count_txt_file` function."""

    def test_correct_word_count(self):
        """Test if the method correctly counts words in a file with 5 words."""
        actual = word_count_txt_file("solutions/test_5_words.txt")
        self.assertEqual(actual, 5, "The word count should be 5.")

    def test_empty_file(self):
        """Test if the method returns 0 for an empty file."""
        actual = word_count_txt_file("solutions/test_empty.txt")
        self.assertEqual(actual, 0, "word count must be 0 for an empty file.")

    def test_multiple_lines_file(self):
        """Test if the method correctly counts words in a multi-line file."""
        actual = word_count_txt_file("solutions/test_multiple.txt")
        self.assertEqual(
            actual, 10, "The word count should be 10 for a multi-line file."
        )

    def test_file_not_exist(self):
        """Test if the method raises an error for a non-existent file."""
        with self.assertRaises(
            AssertionError, msg="An error if the file does not exist."
        ):
            word_count_txt_file("non_existent_file.txt")

    def test_not_a_txt_file(self):
        """Test if the method raises an error for a non-.txt file."""
        with self.assertRaises(
            AssertionError, msg="Should raise an error for a non-.txt file."
        ):
            word_count_txt_file("test")

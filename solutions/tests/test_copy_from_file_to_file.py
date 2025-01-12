"""
This function copies content from one file to another.

Parameters:
    source_file (str): The file to read the content from
    destination_file (str): The file to write the content to

Returns:
    None: The function performs the copying operation but does not return anything

Raises:
    AssertionError: If the source file does not exist
    AssertionError: If the source or destination file is not a .txt file
"""

import unittest

from ..copy_from_file_to_file import copy_file_to_file


class TestCopyFromFileToFile(unittest.TestCase):
    """Test various scenarios for copying content from one file to another"""

    def test_des_not_exist(self):
        """Test when the destination file does not exist"""
        source_file = "solutions/source.txt"
        destination_file = "solutions/destination.txt"

        # Call the function to copy content from source to destination
        copy_file_to_file(source_file, destination_file)

        # Open both files and check if the content matches
        with (
            open("solutions/source.txt", "r") as source,
            open("solutions/destination.txt", "r") as destination,
        ):
            # Assert that content of the source is identical to the destination
            self.assertEqual(source.read(), destination.read())

    def test_copy_to_file(self):
        """Test when the destination file already exists"""
        source_file = "solutions/source.txt"
        destination_file = "solutions/destination.txt"

        # Call the function to copy content from source to destination
        copy_file_to_file(source_file, destination_file)

        # Open both files and compare their content
        with (
            open("solutions/source.txt", "r") as source,
            open("solutions/destination.txt", "r") as destination,
        ):
            # Assert that  content of the source is identical to the destination
            self.assertEqual(source.read(), destination.read())

    def test_not_a_txt_file(self):
        """It raises an assertion error if the source file is not a .txt file"""
        with self.assertRaises(AssertionError):
            # Call the function with a source file that is not a .txt file
            copy_file_to_file("solutions/Source.", "solutions/destination.txt")

    def test_source_file_empty(self):
        """Test when the source file is empty"""
        source_file = "solutions/empty.txt"
        destination_file = "solutions/destination.txt"

        # Copy content from an empty source file to the destination file
        copy_file_to_file(source_file, destination_file)

        # Open both files and compare their content
        with (
            open("solutions/empty.txt", "r") as source,
            open("solutions/destination.txt", "r") as destination,
        ):
            # Assert that both the source and destination are empty (no content)
            self.assertEqual(source.read(), destination.read())

    def test_src_not_exist(self):
        """Test when the source file does not exist"""
        source_file = "solutions/not_exist.txt"
        destination_file = "solutions/destination.txt"

        # Check if it raises an assertion error when the source does not exist
        with self.assertRaises(AssertionError):
            copy_file_to_file(source_file, destination_file)

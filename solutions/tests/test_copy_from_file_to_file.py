import unittest

from ..copy_from_file_to_file import copy_file_to_file

"""
    copy the content from one file to another file
    Parameters:
        source_file (str): the file to read the conent from
        Destination_file(str): the file to add the content to

    Returns ->
    None-The method performs the copying operation but does not return anything
    Raises: AssertionError
"""


class TestCopyFromFileToFile(unittest.TestCase):
    def test_des_not_exist(self):
        """This method test if Destination doesn't exist"""
        source_file = "solutions/source.txt"
        destination_file = "solutions/destination.txt"
        copy_file_to_file(source_file, destination_file)
        with (
            open("solutions/source.txt", "r") as source,
            open("solutions/destination.txt", "r") as destination,
        ):
            self.assertEqual(source.read(), destination.read())

    def test_copy_to_file(self):
        """This method test when the file we copy already exist"""
        source_file = "solutions/source.txt"
        destination_file = "solutions/destination.txt"
        copy_file_to_file(source_file, destination_file)

        with (
            open("solutions/source.txt", "r") as source,
            open("solutions/destination.txt", "r") as destination,
        ):
            self.assertEqual(source.read(), destination.read())

    def test_not_a_txt_file(self):
        """It should raise an assertion error if file is not .txt"""
        with self.assertRaises(AssertionError):
            copy_file_to_file("solutions/Source.", "solutions/destination.txt")

    def test_source_file_empty(self):
        """The method test when the source file is empty"""
        source_file = "solutions/empty.txt"
        destination_file = "solutions/destination.txt"
        copy_file_to_file(source_file, destination_file)

        with (
            open("solutions/empty.txt", "r") as source,
            open("solutions/destination.txt", "r") as destination,
        ):
            self.assertEqual(source.read(), destination.read())

    def test_src_not_exist(self):
        """This method test if Source doesn't exist"""
        source_file = "solutions/not_exist.txt"
        destination_file = "solutions/destination.txt"

        with self.assertRaises(AssertionError):
            copy_file_to_file(source_file, destination_file)

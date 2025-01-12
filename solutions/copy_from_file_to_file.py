"""
This module copies content from one file to another.

Module contents:
    - `source_file` (.txt): the file to read content from.
    - `destination_file` (.txt): the file to write content to.

Created on 1 Jan 2025 "Happy New Year!"
@author: Saja Abusafia
"""

import os


def copy_file_to_file(source_file: str, destination_file: str) -> None:
    """
    Copies content from a source file to a destination file.

    Parameters:
        source_file (str): The file to read the content from.
        destination_file (str): The file to write the content to.

    Returns:
        None:Method performs the copying operation but doesn't return anything.

    Raises:
        AssertionError: If the source file does not exist.
        AssertionError: If the source file is not a .txt file.
        AssertionError: If the destination file is not a .txt file.


    >>> copy_file_to_file("solutions/source.txt", "solutions/destination.txt")

    >>> copy_file_to_file("solutions/empty.txt", "solutions/destination.txt")

    >>> copy_file_to_file("solutions/destination.txt", "solutions/empty.txt")

    """
    # Defensive checks
    assert os.path.exists(source_file), (
        f"Error: Source file '{source_file}' doesn't exist."
    )
    assert source_file.endswith(".txt"), (
        f"Error: Source file '{source_file}' is not a .txt file."
    )
    assert destination_file.endswith(".txt"), (
        f"Error: Destination file '{destination_file}' is not a .txt file."
    )

    # Copy operation: Open the source file in read mode
    with open(source_file, "r") as file_from:
        # Read the entire content of the source file
        file_content = file_from.read()

    # Open the destination file in write mode
    with open(destination_file, "w") as file_to:
        # Write the content read from the source file into the destination file
        file_to.write(file_content)

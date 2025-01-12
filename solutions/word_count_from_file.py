"""
A Module for counting the number of words in a .txt file.

Module contents:
    - Function: `word_count_txt_file` for counting words in a file.
    - Input: `.txt` file to read the content from.
    - Output: Total number of words in the file.

Created on 30 Dec 2024
@author: Saja Abusafia
"""

import os


def word_count_txt_file(file_name) -> int:
    """
    Counts the total number of words in a .txt file.

    Parameters:
        file_name (str): The name of the file to read the content from.

    Returns:
        int: The total number of words in the file.

    Raises:
        AssertionError: If the file does not exist.
        AssertionError: If the file is not a .txt file.

    >>> word_count_txt_file("solutions/test_5.txt")
    5
    >>> word_count_txt_file("solutions/test_empty.txt")
    0
    >>> word_count_txt_file("solutions/test_multiple.txt")
    10
    """

    # Defensive assertions
    assert os.path.exists(file_name), f"Error:file '{file_name}' doesn't exist"
    assert file_name.endswith(".txt"), (
        f"Error: The file '{file_name}' does not have a .txt extension."
    )

    # Open the file safely
    f = open(file_name, "r")
    file_size = os.path.getsize(file_name)

    # Return 0 if the file is empty
    if file_size == 0:
        return 0
    # Read the file's content
    file_content = f.read()

    i = 0
    for n in file_content:
        if n == "":
            i += 1
            break  # Don't increment unless it reach the end of a word
        elif n == " ":
            i += 1  # Increment if the character is a space
        elif n == "\n":
            i += 1  # Increment if reaches the end of a file

    f.close()
    return i

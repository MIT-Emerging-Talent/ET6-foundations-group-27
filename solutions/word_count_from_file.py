import os

"""
A Module for counting the number of words in a .txt file

Module contents:
    - .txt file: the file to read the content from
    - Number: the number of words in the file

created on 30 Dec 2024
@author: saja abusafia
"""


def word_count_txt_file(file_name) -> int:
    """
    The function counts the total number of words in a file

    Parameters:
        String: file_name (str): the file name to read the content from

    Returns:
        int n: The total number of words

    >>> word_count_txt_file("solutions/test_5.txt")
    5
    >>> word_count_txt_file("solutions/test_empty.txt")
    0
    >>> word_count_txt_file("solutions/test_multiple.txt")
    10
    """

    assert os.path.exists(file_name), f"Error:file '{file_name}' doesn't exist"
    assert file_name.endswith(
        ".txt"
    ), f"Error: The file '{file_name}' does not have a .txt extension."

    f = open(file_name, "r")
    file_size = os.path.getsize(file_name)
    if file_size == 0:
        return 0

    file_content = f.read()

    i = 0

    for n in file_content:
        if n == "":
            i += 1
            break
        elif n == " ":
            i += 1  # Increment if the character is a space
        elif n == "\n":
            i += 1  # Increment if reaches the end of a file

    f.close()
    return i

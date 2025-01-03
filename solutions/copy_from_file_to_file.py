import os

"""
    This Module can copy content from one file to another

    Module contents:
    - .txt file: the file to read the content from
    - .txt file: the file to write the content to

created on 1 Jan 2025 "Happy new year"
@author: saja abusafia

"""


def copy_file_to_file(source_file, destination_file):
    """
    The function copies the content from one file to another file


    Parameters:
        source_file (str): the file to read the conent from
        destination_file(str): the file to add the content to

    Returns:
        none-The function performs the copying operation but does not return
        anything

    >>> copy_file_to_file("solutions/source.txt","solutions/destination.txt")



    """
    assert os.path.exists(
        source_file
    ), f"Error: Source file '{source_file}' doesn't exist."
    assert source_file.endswith(
        ".txt"
    ), f"Error: Source file '{source_file}' is not a .txt file."
    assert destination_file.endswith(
        ".txt"
    ), f"Error: Destination file '{destination_file}' is not a .txt file."

    with open(source_file, "r") as file_from:
        file_content = file_from.read()

    with open(destination_file, "w") as file_to:
        file_to.write(file_content)

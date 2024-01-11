#!/usr/bin/python3

"""
Module with the function write_file
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file.

    Args:
        filename: the name of the file.
        text: the text to write.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        my_file.write(text)
        return len(text)

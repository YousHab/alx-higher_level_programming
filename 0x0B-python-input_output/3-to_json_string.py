#!/usr/bin/python3

"""
Module with the fucntion append_write
"""

def append_write(filename="", text=""):
    """
    This fucniton appends a string at the end of
    a text file (UTF8)

    Args:
        filename: the file's name
        text: the text to add.

    Returns:
        The number of appended characters
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        my_file.write(text)
        return len(text)

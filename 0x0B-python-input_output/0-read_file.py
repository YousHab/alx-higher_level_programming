#!/usr/bin/python3

"""
Module with the function read_file
"""


def read_file(filename=""):
    """
    Function that reads a text file UTF8 and
    prints it to stdout.

    Args:
        filename: the file's name.

    """
    with open("filename", 'r', encoding="utf-8") as my_file:
        print(my_file.read())

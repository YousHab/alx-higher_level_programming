#!/usr/bin/python3

"""
==========================
Module of the class Mylist
==========================
"""


class Mylist(list):
    """ Mylist is a class that inherits from list
    """

    def print_sorted(self):
        """ Method that sort a list
        """
        print(sorted(self))

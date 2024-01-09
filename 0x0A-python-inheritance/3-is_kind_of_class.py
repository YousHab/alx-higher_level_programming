#!/usr/bin/python3

"""
=======
Module with the method is_kind_of_clas
=======
"""


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is
    an instance of, or if the object is an instance of a class that
    inherited from, the specified class ; otherwise False.

    Args:
        obj: the object to be tested.
        a_class: the test class.

    Returns:
        True: if the object is an instance of a class that
            inherited from, the specified class.
        False: Otherwise.
    """
    return isinstance(obj, a_class)

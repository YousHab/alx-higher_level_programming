#!/usr/bin/python3

def lookup(obj):
    """ Function that returns the list of available attributes and
    methods of an object

    Args:
        obj: the object.

    Returns:
        a list of available attributes.
    """

    return dir(obj)

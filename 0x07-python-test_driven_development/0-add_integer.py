#!/usr/bin/python3
def add_integer(a, b=98):
    """ Function that return the sum of to number

    Args:
        a: the first integer
        b: the second integer

    Raises:
        TypeError: "a must be an integer" or "b must be an integer"

    Returns: the addition of tow integers.
    """
    types = (int, float)
    if type(a) not in types:
        raise TypeError("a must be an integer")
    if type(b) not in types:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

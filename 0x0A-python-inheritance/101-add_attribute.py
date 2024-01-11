#!/usr/bin/python3

"""
Add attribute function
"""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object if possible.

    Args:
        obj: the object.
        attr_name: the attribute name.
        attr_value: the attribute value.

    Raises:
        TypeError: if it cannot add new attribute.
    """
    if not hasattr(obj, '__dict__') and not isinstance(obj, dict):
        raise TypeError("can't add new attribute")

    obj.__setattr__(attr_name, attr_value)

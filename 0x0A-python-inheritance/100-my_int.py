#!/usr/bin/python3

"""
The class MyInt
"""


class MyInt(int):
    """Custom class MyInt that inherits from int with inverted ==
    and != operators."""

    def __eq__(self, other):
        """Override the == operator."""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Override the != operator."""
        return not super().__ne__(other)

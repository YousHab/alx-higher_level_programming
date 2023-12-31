#!/usr/bin/python3
""" Define the Square class"""


class Square:
    """ Square class
    Attributes:
        size: the size of the square
    """

    def __init__(self, size=0):
        """Creates new instances of square

        Args:
            size: the size of square
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate the area of a square.

        Returns: the area of square
        """
        return self.__size**2

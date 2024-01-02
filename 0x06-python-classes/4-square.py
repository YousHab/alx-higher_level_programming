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

    def area(self):
        """Calculate the area of a square.

        Returns: the area of square
        """
        return self.__size**2
    
    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """Property setter for size.
        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

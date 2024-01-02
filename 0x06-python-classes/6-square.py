#!/usr/bin/python3
""" Define the Square class"""


class Square:
    """ Square class
    Attributes:
        size: the size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances of square

        Args:
            size: the size of square
            position: the position of the square
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Calculate the area of a square.

        Returns: the area of square
        """
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * (self.__size))

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

    @property
    def position(self):
        """ Return the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter for position

        Args:
            value (tuple) : a tuple of 2 positive integers

        Raises:
            TypeError: positon must be a tuple of 2 positive integer
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

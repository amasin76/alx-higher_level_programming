#!/usr/bin/python3
class Square:
    """This module defines a Square class"""

    def __init__(self, size=0):
        """Initialize a new Square object with a given size.

        Args:
            size (int): The size of the new square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The current square area.
        """
        return self.__size**2

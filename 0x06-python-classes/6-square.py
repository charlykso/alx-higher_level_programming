#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """"
        Getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    @property
    def position(self):
        """"
        Getter for position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Setter for position
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Area of square
        """
        return (self.__size)**2

    def my_print(self):
        """Print the area of a square"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print("_", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

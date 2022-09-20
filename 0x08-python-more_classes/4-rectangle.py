#!/usr/bin/python3

"""Define a class Rectangle"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialize a new class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """"
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        returns the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Prints rectangle with #'s """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return rect

    def __repr__(self):
        """ String representation to recreate new instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

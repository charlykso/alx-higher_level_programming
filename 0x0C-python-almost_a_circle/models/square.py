#!/usr/bin/python3
"""
Square that inherits from rectangle
"""


from rectangle import Rectangle

class Square(Rectangle):
    """
    class square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(id, x, y, size, size)
        self.size = size

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        self.width = value
        self.height = value

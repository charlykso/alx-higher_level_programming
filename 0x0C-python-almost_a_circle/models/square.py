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

    def update(self, *args, **kwargs):
        """
        variadic arguments
        """
        argc = len(args)
        if argc > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except BaseException:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.width = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def __str__(self):
        '''
        String representation
        '''
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x, self.y, self.size)

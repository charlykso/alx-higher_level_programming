#!/urs/bin/python3
"""
a function that returns True if the object is an instance of
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Notes:
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of
    Return:
        True if obj is an instance of class that it inherited from
    """
    return isinstance(obj, a_class)

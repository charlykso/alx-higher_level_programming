#!/usr/bin/python3
"""Defines a function that adds two numbers"""


def add_integer(a, b=98):
    """
    Returns a + b as integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

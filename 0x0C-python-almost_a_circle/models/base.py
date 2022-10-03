#!/usr/bin/python3
"""
the first class base
"""


import json


class Base:
    """
    Base class
    """
    
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string returns a JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        json.dumps(list_dictionaries)

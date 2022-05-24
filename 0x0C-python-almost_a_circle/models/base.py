#!/usr/bin/python3
"""the class that is the base of all other classes"""


class Base:
    """base class to manage id attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation of base w/ id attribute"""
        if id is not None:
            self.id = id
        else:
            self.id = __nb_objects += 1

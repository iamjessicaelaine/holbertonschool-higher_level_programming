#!/usr/bin/python3
"""write an empty class BaseGeometry"""


class BaseGeometry:
    """defines an empty class"""
    def __init__(self):
        """instantiation of a empty class"""
        pass

    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")

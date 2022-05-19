#!/usr/bin/python3
"""write a class Rectangle that inherits from class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """birthing BaseGeometry's first child"""
    def __init__(self, width, height):
        """instantiating parent & child attributes & validating values"""
        # validate and define  width & height
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

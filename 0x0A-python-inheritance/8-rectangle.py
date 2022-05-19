#!/usr/bin/python3
"""write a class Rectangle that inherits from class BaseGeometry"""


class BaseGeometry:
    """defines a class BaseGeometry"""

    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """class method which validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """birthing BaseGeometry's first child"""
    def __init__(self, width, height):
        """instantiating parent & child attributes & validating values"""
        # call integer validator method to validate with & height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # defining private instance attributes
        self.__width = width
        self.__height = height

#!/usr/bin/python3
"""write a class BaseGeometry"""


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

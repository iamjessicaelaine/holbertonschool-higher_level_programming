#!/usr/bin/python3
"""function  identifies if obj. is exactly an instance of a specifc class"""


def is_same_class(obj, a_class):
    """returns true if obj arg is instance of a_class arg"""
    if type(obj) is a_class:
        return True
    else:
        return False

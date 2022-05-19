#!/usr/bin/python3
"""function to determine if object is instance of parent and/or child class"""


def is_kind_of_class(obj, a_class):
    """returns true if obj is instance of parent a_class or one of its kids"""
    return(isinstance(obj, a_class))

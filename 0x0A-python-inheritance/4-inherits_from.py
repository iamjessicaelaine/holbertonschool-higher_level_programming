#!/usr/bin/python3
"""function say if obj inherited from a class, either directly or indirectly"""


def inherits_from(obj, a_class):
    """did obj inherit from a_class? find out on the next episode of maury"""
    # need to use type() to get class info to compare to a_class
    if issubclass(type(obj), a_class):  # function will evaluate 2 tru or false
        return True
    else:
        return False

#!/usr/bin/python3
"""a function that returns list of available attributes & methods of an obj"""


def lookup(obj):
    """returns list of object's attributes & methods"""
    return (dir(obj))

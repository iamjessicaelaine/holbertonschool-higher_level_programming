#!/usr/bin/python3
"""function returns dict descrip w/ simple data struct for JSON obj"""


def class_to_json(obj):
    """get dictionary rep of obj"""
    return vars(obj)

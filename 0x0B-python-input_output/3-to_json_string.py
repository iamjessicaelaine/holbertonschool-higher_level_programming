#!/usr/bin/python3
"""module to return JSON stringrep of an object"""


import json


def to_json_string(my_obj):
    """returns JSON string representation of my_obj"""
    jsonstrrep = json.dumps(my_obj)
    return jsonstrrep

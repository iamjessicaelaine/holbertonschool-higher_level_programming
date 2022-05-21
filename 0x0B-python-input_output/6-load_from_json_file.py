#!/usr/bin/python3
"""module creates an object from a 'JSON file'"""


import json


def load_from_json_file(filename):
    """creates an object from filename, a json file"""
    with open(filename, 'r', encoding="utf-8") as j:
        # file must actually be read after it's opened w/ read permission
        redfile = j.read()
        obj = json.loads(redfile)

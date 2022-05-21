#!/usr/bin/python3
"""function appends string to end of txt file"""


def append_write(filename="", text=""):
    """appends text to end of filename & returns chars added"""
    with open(filename, 'a', encoding="utf-8") as j:
        charsadded = j.write(text)
        return charsadded

#!/usr/bin/python3
"""a function that writes a string to a txt file"""


def write_file(filename="", text=""):
    """writes text to filename & returns characters written"""
    with open(filename, 'w', encoding="utf-8") as j:
        charswrote = j.write(text)
        return charswrote

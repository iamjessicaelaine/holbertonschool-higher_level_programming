#!/usr/bin/python3
"""a module to read a text file"""


def read_file(filename=""):
    """function reads a txt file and prints it to stdout"""
    with open(filename, encoding="utf-8") as j:
        redfile = j.read()
        print(redfile)

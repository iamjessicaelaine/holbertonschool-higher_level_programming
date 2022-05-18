#!/usr/bin/python3
"""write a class MyList that inherits from list"""


class MyList(list):
    """defining child class, MyList, which inherits from list"""
    def print_sorted(self):
        """this method prints list sorted in ascending order"""
        print(sorted(self))  

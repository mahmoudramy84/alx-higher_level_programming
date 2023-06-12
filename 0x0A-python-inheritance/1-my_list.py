#!/usr/bin/python3
"""Module that inherits from the list class"""


class MyList(list):
    """A class that inherit from list"""
    def print_sorted(self):
        """Prints asorted list"""
        print(sorted(self))
        
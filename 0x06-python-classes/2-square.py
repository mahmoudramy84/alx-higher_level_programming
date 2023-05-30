#!/usr/bin/python3
"""defines a square with Private instance attribute: size"""


class Square:
    """Private instance attribute: size"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

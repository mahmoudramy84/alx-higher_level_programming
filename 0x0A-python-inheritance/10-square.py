#!/usr/bin/python3
"""Defines a class Square"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """this class represents a square using a Rectangle"""

    def __init__(self, size):
        """Instantiation anew square with size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

#!/usr/bin/python3
"""This module contains a class to serve as base for other classes"""


class Base:
    """ the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
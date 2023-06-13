#!/usr/bin/python3
"""This module defines JSON Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON """
    with open(filename, "w") as file:
        json.dumps(my_obj, file)

#!/usr/bin/python3
"""This module defines atext appending to afile"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and,
    returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)

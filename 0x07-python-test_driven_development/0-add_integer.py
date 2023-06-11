#!/usr/bin/python3
"""contains a function that adds 2 integers."""


def add_integer(a, b=98):
    """
    function that returns an integer
    args:
        a (int or float): first param
        b (int or float): second param
    Returns: 
        the addition of a and b
    Raisees:
    TypeError with message if a and b isn,t integers or floats
    """
    if type(a) not in [int, float]:
        raise TypeError ("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError ("b must be an integer")
    return int(a) + int(b)

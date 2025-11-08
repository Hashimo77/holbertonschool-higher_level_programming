#!/usr/bin/python3
"""Return list of available attributes and methods of an object."""


def lookup(obj):
    """Return a list of attributes and methods of obj."""
    return dir(obj)

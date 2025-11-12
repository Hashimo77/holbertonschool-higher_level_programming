#!/usr/bin/python3
"""Module that contains the function class_to_json."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structures
    for JSON serialization.

    Args:
        obj: The object to serialize.

    Returns:
        dict: Dictionary representation of the object."""
    return obj.__dict__

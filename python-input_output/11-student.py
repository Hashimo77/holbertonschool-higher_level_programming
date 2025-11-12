#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization/deserialization."""


class Student:
    """Defines a student with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: Dictionary representation of the object, filtered if attrs provided.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            new_dict = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    new_dict[k] = v
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance from a dictionary.

        Args:
            json (dict): Dictionary with keys as attribute names and values as attribute values.
        """
        for k, v in json.items():
            setattr(self, k, v)

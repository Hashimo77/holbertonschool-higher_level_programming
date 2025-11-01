#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Returns a new list with all occurrences of search replaced by replace."""
    return [replace if x == search else x for x in my_list]

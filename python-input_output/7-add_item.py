#!/usr/bin/python3
"""Script that adds all arguments to a Python list,
and then saves them to a JSON file."""
import sys
from pathlib import Path

save_to_json_file = __import__(
    '5-save_to_json_file').save_to_json_file
load_from_json_file = __import__(
    '6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

# Check if file exists and load the list, otherwise start with empty list
if Path(filename).is_file():
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add all arguments to the list
my_list.extend(sys.argv[1:])

# Save updated list back to file
save_to_json_file(my_list, filename)

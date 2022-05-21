#!/usr/bin/python3
"""adds cmd line args to a Python list & saves them to file"""


import sys  # module needed to retrieve cmd line args
import json  # importing just in case following imports need it

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    # load the arguments or create an empty list
    pylist = load_from_json_file("add_item.json")
except(TypeError, FileNotFoundError):
    pylist = []  # if load function fails, create empty list

# now we can add
for arg in sys.argv[1:]:  # starting at 1st arg loop thru args
    pylist.append(arg)  # add the arguments to the list

# list has been created, time to save it
save_to_json_file(pylist, "add_item.json")

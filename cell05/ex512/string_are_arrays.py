#!/usr/bin/env python3
# string_are_arrays.py

import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    result = ""

    for char in text:
        if char == "z":
            result += "z"

    if result == "":
        print("none")
    else:
        print(result)
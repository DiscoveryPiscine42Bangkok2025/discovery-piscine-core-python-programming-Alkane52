#!/usr/bin/env python3
# count_it.py

import sys

if len(sys.argv) == 1:
    print("none")
else:
    params = sys.argv[1:]
    print("parameters:", len(params))

    for word in params:
        print(word + ":", len(word))
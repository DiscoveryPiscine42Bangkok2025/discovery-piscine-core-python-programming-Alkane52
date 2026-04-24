#!/usr/bin/env python3
# advanced_mult.py

import sys

if len(sys.argv) > 1:
    print("none")
else:
    table = 0

    while table <= 10:
        print("Table de", table, ":", sep="", end="")

        i = 0
        while i <= 10:
            print(table * i, end="")
            if i < 10:
                print(" ", end="")
            i += 1

        print()
        table += 1
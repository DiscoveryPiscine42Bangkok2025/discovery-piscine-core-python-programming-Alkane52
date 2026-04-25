#!/usr/bin/env python3
# downcase_all.py

import sys

def downcase_it(text):
    return text.lower()

if len(sys.argv) == 1:
    print("none")
else:
    for word in sys.argv[1:]:
        print(downcase_it(word))
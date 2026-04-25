#!/usr/bin/env python3
# greetings_for_all.py

def greetings(name="noble stranger"):
    if type(name) == str:
        print("Hello, " + name + ".")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
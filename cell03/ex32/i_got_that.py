#!/usr/bin/env python3
# i_got_that.py

text = ""

while text != 1:
    text = input("Say something: ")
    if text == "STOP":
        print("I GOT THAT")
        break
#!/usr/bin/env python3
# to25.py

number = int(input("Enter a number: "))

if number > 25:
    print("Error")
else:
    while number <= 25:
        print(number)
        number += 1
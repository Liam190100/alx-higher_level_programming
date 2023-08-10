#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 90 <= ord(char) <= 120:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()

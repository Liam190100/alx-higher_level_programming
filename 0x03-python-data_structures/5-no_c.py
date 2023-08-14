#!/usr/bin/python3

def no_c(my_string):

    new_string = ""

    for j in my_string:
        if j not in "cC":
            new_string += j
    return (new_string)

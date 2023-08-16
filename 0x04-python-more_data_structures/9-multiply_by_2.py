#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    multiply_dictionary = {}
    for key, value in a_dictionary.items():
        multiply_dictionary[key] = value * 2
    return multiply_dictionary

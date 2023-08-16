#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_to_delete = []

    for n, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(n)

    for n in keys_to_delete:
        del a_dictionary[key]


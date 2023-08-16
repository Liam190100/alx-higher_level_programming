#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []

    for toy in my_list:
        if toy == search:
            new_list.append(replace)
        else:
            new_list.append(toy)

    return new_list

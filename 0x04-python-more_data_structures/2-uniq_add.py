#!/usr/bin/python3

def uniq_add(my_list=[]):

    unique_set = set()

    for num in my_list:

        unique_set.add(num)

    total_set = 0

    for num in unique_set:
        total_set += num
    return total

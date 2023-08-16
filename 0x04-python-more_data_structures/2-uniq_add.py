#!/usr/bin/python3

def uniq_add(my_list=[]):

    unique_set = set()

    for j in my_list:

        unique_set.add(j)

    total_sum = 0

    for j in unique_set:
        total_sum += j
    return total_sum

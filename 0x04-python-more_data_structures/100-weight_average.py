#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    num_weighted_sum = 0
    num_weight = 0

    for score, weight in my_list:
        num_weighted_sum += score * weight
        num_weight += weight

    weighted_average = num_weighted_sum / num_weight
    return weighted_average

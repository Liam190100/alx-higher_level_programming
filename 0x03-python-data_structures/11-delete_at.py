#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list  

    result_list = []
    for n in range(len(my_list)):
        if n != idx:
            result_list.append(my_list[n])

    return result_list

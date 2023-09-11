#!/usr/bin/python3
"""
This is module function
"""


class MyList(list):
    """
    This class contains a fuction
    """
    def print_sorted(self):
        """
        Class MyList which inherits the list
        """
        sorted_list = sorted(self)
        print(sorted_list)

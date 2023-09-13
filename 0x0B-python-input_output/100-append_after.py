#!/usr/bin/python3

"""
Module that append and adds lines to the files
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line into a file
        search_string: line in file to search
        new_string: string to insert into file
    """
    lines = []
    output = []
    with open(filename, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            output.append(line)
            if (line.count(search_string)):
                output.append(new_string)
        f.seek(0)
        f.truncate(0)
        f.writelines(output)

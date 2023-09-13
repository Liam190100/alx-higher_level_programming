#!/usr/bin/python3
"""Script that computes the metrics"""


import sys


# Initialize the total file
total_size = 0
status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }


def print_stats():
    """Prints the statistics in file"""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))


try:
    # Loop through the lines in the stdin
    for i, line in enumerate(sys.stdin, 1):
        # Split the line using spaces
        tokens = line.split()
        if len(tokens) > 2:
            size = tokens[-1]
            code = tokens[-2]
            if size.isdigit():
                total_size += int(size)
            if code in status_codes:
                status_codes[code] += 1
        if i % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt:

    print_stats()
    raise

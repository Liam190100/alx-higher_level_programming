#!/usr/bin/python3
"""
Script that reads stdin line by line and computes the metrics
"""
import sys


codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
len = 0
total_size = 0
status_counts = {code: 0 for code in codes}

try:
    for line in sys.stdin:
        len += 1
        line = line.strip()
        words = line.split()
        total_size += int(words[8])

        status_code = words[7]
        if status_code in codes:
            status_counts[status_code] += 1

        if len % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_counts):
                if status_counts[code] != 0:
                    print("{}: {}".format(code, status_counts[code]))

except KeyboardInterrupt as e:
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] != 0:
            print("{}: {}".format(code, status_counts[code]))
    print(e)

#!/usr/bin/python3
for a in range(10):
    for b in range(a + 1, 10):
        if a == 0 and b == 1:
            continue
        if a < 9 or b < 9:
            print("{:d}{:d}, ".format(a, b), end="")
        else:
            print("{:d}{:d}".format(a, b))


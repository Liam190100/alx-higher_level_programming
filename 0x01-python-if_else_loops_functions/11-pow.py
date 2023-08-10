#!/usr/bin/python3
def pow(a, b):
    power = 1
    for c in range(abs(b)):
        power *= a
    if b < 0:
        power = 1 / power
    return power

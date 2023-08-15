#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for n in range(len(row)):
            if n == len(row) - 1:
                print("{:d}".format(row[n]), end="")
            else:
                print("{:d} ".format(row[n]), end="")
        print()

#!/usr/bin/python3
"""Function list Pascal’s triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s
    triangle

    Args:
        n (int): numbers of rows in triangle

    Returns:
        list of int: triangle
    """
    # Returns an empty list if n <= 0
    if n <= 0:
        return []

    # Initialize the triangle with the top row
    triangle = [[1]]

    for row in range(1, n):
        prev_row = triangle[row - 1]
        curr_row = [1]

        for col in range(1, row):
            curr_element = prev_row[col - 1] + prev_row[col]
            curr_row.append(curr_element)
        curr_row.append(1)
        triangle.append(curr_row)

    return triangle

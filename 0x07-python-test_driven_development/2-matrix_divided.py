#!/usr/bin/python3
"""
this module is composed by a function that divides the numberss of a matrix

"""


def matrix_divided(matrix, div):
    """ int/float numbers of a matrix

    Args:
        matrix (list of lists): The matrix to be divided. Must be a list of lists of integers or floats
        div:(int or float): matrix

    Returns:
        A matrix of result after div

    Raises:
        TypeError: If `matrix` is not a list of lists of integers/floats,
               if each row of the matrix does not have the same size,
               or if `div` is not a number (integer or float).

        ZeroDivisionError: If div is 0


    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(msg_size)

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msg_type)

        len_e = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)

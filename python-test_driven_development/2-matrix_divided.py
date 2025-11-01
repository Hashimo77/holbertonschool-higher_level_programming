#!/usr/bin/python3
"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.

    Returns:
        list: A new matrix with all elements divided by div and rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   or rows are not of the same size,
                   or div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if len(matrix) == 0 or any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]

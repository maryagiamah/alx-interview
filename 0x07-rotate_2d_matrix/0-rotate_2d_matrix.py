#!/usr/bin/python3
"""
Rotate a matrix 90 degress clockwise
- Transpose the matrix
    (exchange the rows and columns)
- Reverse the matrix after

Note: A rotated 90 degree matrix
    must have it first row as its last column

"""


def rotate_2d_matrix(matrix):
    """Rotate matrix 90deg clockwise"""

    # Transpose Matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Now reverse matrix
    for row in matrix:
        row.reverse()

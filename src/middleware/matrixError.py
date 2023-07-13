def matrixError(matrix, length):
    if any(len(row) != length for row in matrix):
        raise ValueError(
            'Invalid matrix dimensions. The matrix must be square (NxN).')

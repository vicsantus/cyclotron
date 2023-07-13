def matrixError(matrix, length):
    num_cols = len(matrix[0]) if length > 0 else 0

    if length != num_cols:
        raise ValueError(
            'Invalid matrix dimensions. The matrix must be square (NxN).')

def matrixError(matrix, size):
    if size <= 3:
        raise ValueError(
            'Invalid matrix dimensions. The matrix must be minimum 4x4.'
        )
    if any(len(row) != size for row in matrix):
        raise ValueError(
            'Invalid matrix dimensions. The matrix must be square (NxN).')

def matrixError(matrix, size):
    # Retorna um erro caso a matriz seja menor/igual a 3
    if size <= 3:
        raise ValueError(
            'Invalid matrix dimensions. The matrix must be minimum 4x4.'
        )

    # Retorna um erro caso a matriz não seja quadratica
    if any(len(row) != size for row in matrix):
        raise ValueError(
            'Invalid matrix dimensions. The matrix must be square (NxN).')

    # Retorna um erro caso a matriz uma lista de listas
    if any(isinstance(row, list) for row in matrix):
        raise ValueError(
            'Invalid matrix. The matrix must be list of lists.')

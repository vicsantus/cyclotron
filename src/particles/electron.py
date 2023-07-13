def electron(matrix, particle, size):
    matrix[0] = [particle] * len(matrix[0])
    for i in range(size):
        matrix[i][size-1] = particle
    return matrix

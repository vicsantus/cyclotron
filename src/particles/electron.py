def electron(matrix, particle, size):
    # Substitui a primeira linha da matriz pelo valor particle
    matrix[0] = [particle] * len(matrix[0])

    # Substitui a ulima coluna da matriz pelo valor particle
    for i in range(size):
        matrix[i][size-1] = particle
    return matrix

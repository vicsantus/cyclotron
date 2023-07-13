def proton(matrix, particle, size):
    finalElement = matrix[-1][-1]

    matrix[0] = [particle] * len(matrix[0])

    for i in range(size):
        matrix[i][0] = particle
        matrix[size-1][i] = particle
        matrix[i][size-1] = particle

    matrix[-1][-1] = finalElement
    matrix[-2][-2] = particle

    return matrix

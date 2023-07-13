def proton(matrix, particle, size):
    # Salva o ultimo elemento da matriz para utilizar depois
    finalElement = matrix[-1][-1]

    # Substitui a primeira linha da matriz pelo valor particle
    matrix[0] = [particle] * len(matrix[0])

    # Substitui a ultima coluna, a primeira coluna
    # e a ultima linha por particle
    for i in range(size):
        matrix[i][0] = particle
        matrix[size-1][i] = particle
        matrix[i][size-1] = particle

    # Substitui o ultimo elemento da ultima linha pelo
    # valor original
    # Em seguida, substitui o penultimo elemento da penultima linha
    # por particle
    matrix[-1][-1] = finalElement
    matrix[-2][-2] = particle

    return matrix

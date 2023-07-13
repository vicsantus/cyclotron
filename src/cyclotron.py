from particles.neutron import neutron
from middleware.particleError import particleError
from middleware.matrixError import matrixError


def cyclotron(particle, matrix):
    particleError(particle)
    size = len(matrix)
    matrixError(matrix, size)

    if particle == 'n':
        matrix = neutron(matrix)

    return matrix


if __name__ == '__main__':
    print(
        cyclotron('n', [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))

from particles.neutron import neutron
from particles.electron import electron
from middleware.particleError import particleError
from middleware.matrixError import matrixError


def cyclotron(particle, matrix):
    particleError(particle)
    size = len(matrix)
    matrixError(matrix, size)

    if particle == 'n':
        matrix = neutron(matrix)

    elif particle == 'e':
        matrix = electron(matrix, size)

    return matrix


if __name__ == '__main__':
    print(
        cyclotron('e', [[1, 1, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1]]))

from particles.neutron import neutron
from particles.electron import electron
from particles.proton import proton
from middleware.particleError import particleError
from middleware.matrixError import matrixError


def cyclotron(particle, matrix):
    particleError(particle)
    size = len(matrix)
    matrixError(matrix, size)

    if particle == 'n':
        matrix = neutron(matrix)

    if particle == 'e':
        matrix = electron(matrix, particle, size)

    if particle == 'p':
        matrix = proton(matrix, particle, size)

    return matrix


if __name__ == '__main__':
    print(
        cyclotron('p', [[1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1]]))

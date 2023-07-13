# Importação das particulas e dos casos de erro
from particles.neutron import neutron
from particles.electron import electron
from particles.proton import proton
from middleware.particleError import particleError
from middleware.matrixError import matrixError


def cyclotron(particle, matrix):
    # Verifica se o tipo de partícula é válido
    particleError(particle)
    size = len(matrix)

    # Verifica se a matriz é quadrada (NxN)
    matrixError(matrix, size)

    # Aplica as transformações para a partícula neutron
    if particle == 'n':
        matrix = neutron(matrix)

    # Aplica as transformações para a partícula electron
    if particle == 'e':
        matrix = electron(matrix, particle, size)

    # Aplica as transformações para a partícula proton
    if particle == 'p':
        matrix = proton(matrix, particle, size)

    return matrix


# if __name__ == '__main__':
    # Exemplo de chamada da função cyclotron com uma matriz 6x6 e partícula 'p'
    # print(
    #     cyclotron('p', [[1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1],
    #                     [1, 1, 1, 1, 1, 1],
    #                     'qwerty']))

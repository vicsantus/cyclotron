from src.particles.proton import proton


def testa_se_funcao_proton_funciona_corretamente():
    mock_entrada = [[1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1]]
    mock_entrada2 = [[1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1]]
    mock_saida = [['p', 'p', 'p', 'p', 'p'],
                  ['p', 1, 1, 1, 'p'],
                  ['p', 1, 1, 1, 'p'],
                  ['p', 1, 1, 'p', 'p'],
                  ['p', 'p', 'p', 'p', 1]]

    retorno_proton = proton(mock_entrada, 'p', 5)

    assert retorno_proton == mock_saida
    assert retorno_proton != mock_entrada2

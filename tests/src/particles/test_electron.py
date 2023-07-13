from src.particles.electron import electron


def testa_se_funcao_electron_funciona_corretamente():
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
    mock_saida = [['e', 'e', 'e', 'e', 'e'],
                  [1, 1, 1, 1, 'e'],
                  [1, 1, 1, 1, 'e'],
                  [1, 1, 1, 1, 'e'],
                  [1, 1, 1, 1, 'e']]

    retorno_electron = electron(mock_entrada, 'e', 5)

    assert retorno_electron == mock_saida
    assert retorno_electron != mock_entrada2

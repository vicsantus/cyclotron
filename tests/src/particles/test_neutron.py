from src.particles.neutron import neutron


def testa_se_funcao_neutron_funciona_corretamente():
    mock_entrada = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    mock_entrada2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    mock_saida = [['n', 'n', 'n'], [1, 1, 1], [1, 1, 1]]

    retorno_neutron = neutron(mock_entrada)

    assert retorno_neutron == mock_saida
    assert retorno_neutron != mock_entrada2

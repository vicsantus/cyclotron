import pytest

from src.middleware.particleError import particleError


def testa_se_middleware_particleError_funciona_corretamente():
    error_dimension = 'Invalid particle type. The particle must be "n", "p", or "e".'

    with pytest.raises(ValueError, match=error_dimension):
        particleError('x')

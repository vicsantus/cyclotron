import pytest
import re

from src.middleware.matrixError import matrixError


def testa_se_middleware_matrixError_dimensionError_funciona_corretamente():
    mock_entrada_wrong = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    error_dimension = 'Invalid matrix dimensions. The matrix must be minimum 4x4.'

    with pytest.raises(ValueError, match=error_dimension):
        matrixError(mock_entrada_wrong, 3)


def testa_se_middleware_matrixError_squareError_funciona_corretamente():
    mock_entrada_wrong = [[1, 1, 1, 1, 1],
                          [1, 1, 1, 1],
                          [1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1]]
    error_square = 'Invalid matrix dimensions. The matrix must be square (NxN).'

    with pytest.raises(ValueError, match=re.escape(error_square)):
        matrixError(mock_entrada_wrong, 5)


def testa_se_middleware_matrixError_listOfLists_funciona_corretamente():
    mock_entrada_right = [[1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1]]
    error_list_of_list = 'Invalid matrix. The matrix must be list of lists.'

    with pytest.raises(ValueError, match=error_list_of_list):
        matrixError(mock_entrada_right, 5)

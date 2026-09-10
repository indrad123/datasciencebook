import numpy as np
import pytest

from datasciencebook.matrices import as_matrix, matrix_product, solve_system


def test_valid_matrix_calculations():
    matrix = as_matrix([[2, 1], [1, 3]])
    assert matrix.shape == (2, 2)
    assert matrix_product(matrix, [42, 16]).tolist() == pytest.approx([100, 90])
    solution, residual, condition = solve_system(matrix, [100, 90])
    assert solution.tolist() == pytest.approx([42, 16])
    assert residual.tolist() == pytest.approx([0, 0])
    assert condition > 1


def test_invalid_matrices_rejected():
    with pytest.raises(ValueError):
        as_matrix([])
    with pytest.raises(ValueError):
        matrix_product([[1, 2]], [1])
    with pytest.raises(ValueError):
        solve_system([[1, 1], [2, 2]], [3, 6])
    with pytest.raises(ValueError):
        solve_system([[1, 2, 3], [4, 5, 6]], [1, 2])

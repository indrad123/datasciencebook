import pytest

from datasciencebook.vectors import cosine_similarity, dot_product, euclidean_distance, magnitude, manhattan_distance, unit_vector


def test_valid_vector_calculations():
    assert magnitude([3, 4]) == pytest.approx(5)
    assert unit_vector([3, 4]) == pytest.approx([0.6, 0.8])
    assert dot_product([1, 2, 3], [4, 0, -1]) == 1
    assert euclidean_distance([4, 3, 5], [2, 4, 6]) == pytest.approx(6 ** 0.5)
    assert manhattan_distance([4, 3, 5], [2, 4, 6]) == 4
    assert cosine_similarity([1, 2], [2, 4]) == pytest.approx(1)


def test_invalid_vectors_rejected():
    with pytest.raises(ValueError):
        magnitude([])
    with pytest.raises(ValueError):
        dot_product([1], [1, 2])
    with pytest.raises(ValueError):
        unit_vector([0, 0])
    with pytest.raises(ValueError):
        cosine_similarity([0, 0], [1, 2])

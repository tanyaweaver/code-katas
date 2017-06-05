import pytest
from src.search_rotated_list import find_num_rotated, search


TEST1 = [
    ([1, 2, 3, 4, 5], 0),
    ([4, 5, 1, 2, 3], 2),
    ([1], 0),
    ([4, 5, 6, 7, 1], 4),
    ([], 0),
    ([2, 1], 1)
]


TEST2 = [
    ([1, 2, 3, 4, 5], 3, True),
    ([4, 5, 1, 2, 3], 1, True),
    ([1], 1, True),
    ([4, 5, 6, 7, 1], 10, False),
    ([], 2, False),
    ([2, 1], 3, False)
]


@pytest.mark.parametrize('l, num_rot', TEST1)
def test_num_rotated(l, num_rot):
    assert find_num_rotated(l) == num_rot


@pytest.mark.parametrize('l, num, result', TEST2)
def test_search(l, num, result):
    assert search(l, num) == result

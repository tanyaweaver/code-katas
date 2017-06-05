import pytest
from src.mergesort import merge_sort, merge


TEST1 = [
    ([4], [2], [2, 4]),
    ([1, 3, 5], [2, 5, 6], [1, 2, 3, 5, 5, 6]),
    ([], [1, 2], [1, 2]),
    ([], [], [])
]

TEST2 = [
    ([2, 6, 3, 8, 4, 9], [2, 3, 4, 6, 8, 9]),
    ([1, 2, 3], [1, 2, 3]),
    ([], []),
    (None, None)
]


@pytest.mark.parametrize('l1, l2, result', TEST1)
def test_merge(l1, l2, result):
    assert merge(l1, l2) == result


@pytest.mark.parametrize('l, sorted', TEST2)
def test_merge_sort(l, sorted):
    assert merge_sort(l) == sorted

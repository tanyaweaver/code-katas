import pytest
from src.sublist_max_sum import sublist_max_sum

TEST = [
    ([], None),
    (None, None),
    ([-2, 2, 5, -6, 11], 12),
    ([-5, -3, -6, -1], -1),
    ([0, -2, -4, -1], 0),
    ([9, -8, 4, 2, -5, 10], 12)
]


@pytest.mark.parametrize('arr, max_sum', TEST)
def test_sublist_max_sum(arr, max_sum):
    assert sublist_max_sum(arr) == max_sum

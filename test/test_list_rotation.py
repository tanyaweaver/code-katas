import pytest
from src.list_rotation import list_rotation

TEST = [
    ([1, 2, 3, 4], 1, [4, 1, 2, 3]),
    ([1, 2, 3, 4], 2, [3, 4, 1, 2]),
    ([], 5, []),
    ([1, 2], 5, [1, 2]),
    ([1, 2, 3, 4], -1, [2, 3, 4, 1]),
    ([1, 2, 3, 4], -2, [3, 4, 1, 2]),
    (None, 5, None),
    ([1, 2, 3, 4], 0, [1, 2, 3, 4])
]


@pytest.mark.parametrize('l, number, result', TEST)
def test_rotation(l, number, result):
    assert list_rotation(l, number) == result


@pytest.mark.parametrize('l, number, result', TEST)
def test_rotation1(l, number, result):
    assert list_rotation(l, number) == result

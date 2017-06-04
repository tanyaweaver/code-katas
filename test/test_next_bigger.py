import pytest
from src.next_bigger import next_bigger

TEST = [
    ([8, 9, 1, 3, 2, 5, 6, 4, 1, 8, 1], [9, -1, 3, 5, 5, 6, 8, 8, 8, -1, -1]),
    ([2, 1], [-1, -1]),
    ([7, 5, 3, 2], [-1, -1, -1, -1]),
    ([], [])
]


@pytest.mark.parametrize('l1, result', TEST)
def test_next_bigger(l1, result):
    assert next_bigger(l1) == result

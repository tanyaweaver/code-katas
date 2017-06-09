import pytest
from src.binary_search import binary_search


TEST = [
    ([1, 3, 4, 5, 6, 7], 2, False),
    ([1, 3, 4, 5, 6, 7], 3, True),
    ([], 3, False)
]


@pytest.mark.parametrize('l, num, result', TEST)
def test_binary_search(l, num, result):
    assert binary_search(l, num) == result

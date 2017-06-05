import pytest
from src.reverse_k_llist import Llist


LIST = [
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([], []),
    (None, [])
]

TEST = [
    ([1, 2, 3, 4, 5, 6, 7, 8], 3, [3, 2, 1, 6, 5, 4, 8, 7]),
    ([], 5, []),
    ([1, 2, 3], 4, [3, 2, 1]),
    ([1], 1, [1]),
    ([1, 2], 1, [1, 2]),
    ([1, 2, 3, 4], 2, [2, 1, 4, 3]),
    ([1, 2], 0, [1, 2]),
    ([1, 2], 3.6, [1, 2])
]


@pytest.mark.parametrize('l, result', LIST)
def test_list_add_print(l, result):
    llist = Llist(l)
    assert llist.print_list() == result


@pytest.mark.parametrize('l, k, result', TEST)
def test_reverse_k1(l, k, result):
    llist = Llist(l)
    llist.reverse_k_elements(k)
    assert llist.print_list() == result

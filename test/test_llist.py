import pytest
from src.insert_in_sorted_ll import LinkedList, sum_2_lists

TEST = [
    ([1, 2, 3], [2, 4, 6], [3, 6, 9]),
]


@pytest.mark.parametrize('l1, l2, result', TEST)
def test_sum2(l1, l2, result):
    l1_ = LinkedList()
    for x in l1:
        l1_.add_to_tail(x)
    l2_ = LinkedList()
    for y in l2:
        l2_.add_to_tail(y)
    assert sum_2_lists(l1_, l2_).print_list() == result

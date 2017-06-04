import pytest
from src.common_elements import (common_elements1,
                                 common_elements2,
                                 common_elements3)


TEST = [
    ([1, 2, 3], [3, 5, 6], [3]),
    ([1, 2, 3], [2, 4, 5, 6, 3, 6], [2, 3]),
    ([1, 2, 2, 3], [3, 2, 2, 7], [2, 3]),
    ([], [], None),
    ([], [1], None),
    ([2], [], None),
    (None, [1], None),
    (None, None, None)
]


@pytest.mark.parametrize('l1, l2, result', TEST)
def test_common_elements1(l1, l2, result):
    assert common_elements1(l1, l2) == result


@pytest.mark.parametrize('l1, l2, result', TEST)
def test_common_elements2(l1, l2, result):
    assert common_elements2(l1, l2) == result


@pytest.mark.parametrize('l1, l2, result', TEST)
def test_common_elements3(l1, l2, result):
    if l1 and l2:
        l1.sort()
        l2.sort()
    assert common_elements3(l1, l2) == result

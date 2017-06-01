from src.sorted_square_array import sorted_square_array


def test_sorted1():
    array = [1, 2, 3]
    assert sorted_square_array(array) == [1, 4, 9]


def test_sorted2():
    array = [-2, 1, 3]
    assert sorted_square_array(array) == [1, 4, 9]


def test_sorted3():
    array = [-3, -2, -1]
    assert sorted_square_array(array) == [1, 4, 9]


def test_sorted4():
    array = []
    assert sorted_square_array(array) == []

from src.queen_attack import under_queen_attack


def test_attack1():
    assert under_queen_attack(3, [[0,0]], [[1,1], [0,2], [1, 2]]) == [True, True, False]


queens1 = [[0, 0], [2, 2]]
querries1 = [[1, 2], [2, 0]]


def test_attack2():
    assert under_queen_attack(3, queens1, querries1) == [True, True]


def test_attack3():
    assert under_queen_attack(3, [], [[1, 1]]) == [False]


def test_attack4():
    assert under_queen_attack(3, [], []) == []

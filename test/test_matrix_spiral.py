from src.matrix_spiral import matrix_spiral


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix2 = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 10],
    [11, 12, 13, 14],
    [15, 16, 17, 18]
]

result2 = [1, 2, 3, 4, 7, 10, 14, 18, 17, 16, 15, 11, 7, 4, 5, 6, 9, 13, 12, 8]

matrix3 = [[], []]
result3 = []

matrix4 = []
result4 = []


def test_matrix_spiral1():
    assert matrix_spiral(matrix1) == result1


def test_matrix_spiral2():
    assert matrix_spiral(matrix2) == result2


def test_matrix_spiral3():
    assert matrix_spiral(matrix3) == result3


def test_matrix_spiral4():
    assert matrix_spiral(matrix4) == result4

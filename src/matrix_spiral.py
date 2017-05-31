from itertools import chain


# def matrix_spiral(matrix):
#     """
#     Assuming all rows are the same length
#     """
#     result = []
#     if matrix is None:
#         return None
#     if len(matrix) == 0:
#         return result
#     if len(matrix[0]) == 0:
#         return result
#     i = 0
#     j = len(matrix) - 1
#     k = 0
#     m = len(matrix[0]) - 1
#
#     while i <= j and k <= m:
#         upper = [x for x in matrix[i][k:m+1]]
#         right = [y[m] for y in matrix[i+1:j]]
#         bottom = [x for x in matrix[j][m:k-1:-1]]
#         if k == 0:
#             bottom = [x for x in matrix[j][m:None:-1]]
#         if i == j:
#             bottom = []
#         left = [y[k] for y in matrix[j-1:i:-1]]
#         for element in chain(upper, right, bottom, left):
#             result.append(element)
#         i += 1
#         j -=1
#         k += 1
#         m -= 1
#
#     return result


def matrix_spiral(matrix):
    return matrix and list(matrix.pop(0)) + matrix_spiral(zip(*matrix)[::-1])

from collections import deque


def sorted_square_array(array):
    result = []
    stack = deque()
    i = 0
    while i < len(array) and array[i] < 0:
        stack.append(array[i])
        i += 1
    while len(stack) != 0:
        cur = stack.pop()
        while i < len(array) and array[i] < abs(cur):
            result.append(array[i] ** 2)
            i += 1
        result.append(cur ** 2)
    if i < len(array):
        rest_of_array = array[i:]
        for x in rest_of_array:
            result.append(x ** 2)
    return result

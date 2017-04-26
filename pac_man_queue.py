from collections import deque


def flood(i, j, N, matrix):
    q = deque()
    q.append((i, j))
    while len(q) != 0:
        n, m = q.popleft()
        enemy_or_one = (matrix[n][m] == 1 or matrix[n][m] == 8)
        pac_man = (matrix[n][m] == 3)
        if not enemy_or_one:
            if not pac_man:
                matrix[n][m] = 1
            for i, j in ((n+1, m), (n-1, m), (n, m-1), (n, m+1)):
                inside_matrix = (i in range(N) and j in range(N))
                if inside_matrix and matrix[i][j] != 3 and matrix[i][j] != 1:
                    q.append((i, j))

    return matrix


def pac_man(N, PM, enemies):
    matrix = [[0 for x in range(N)] for y in range(N)]
    i, j = PM
    matrix[i][j] = 3
    for enemy in enemies:
        matrix[enemy[0]] = [8 for x in range(N)]
        for row in matrix:
            row[enemy[1]] = 8
    matrix = flood(i, j, N, matrix)
    count_ones = 0
    for row in matrix:
        for number in row:
            if number == 1:
                count_ones += 1
    return count_ones


if __name__ == '__main__':
    pac_man(10, [3, 0], [[1, 2]])

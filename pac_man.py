def flood(i, j, N, matrix):
    if i not in range(N) or j not in range(N):
        return matrix
    if matrix[i][j] == 1 or matrix[i][j] == 8:
        return matrix
    if matrix[i][j] != 3:
        matrix[i][j] = 1
    matrix = flood(i+1, j, N, matrix)
    matrix = flood(i-1, j, N, matrix)
    matrix = flood(i, j-1, N, matrix)
    matrix = flood(i, j+1, N, matrix)
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
    pac_man(10, [3, 0], [[1, 2], [6, 4]])

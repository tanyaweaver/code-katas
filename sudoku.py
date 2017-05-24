def sudoku2(grid):
    criterion = True
    grid_groups = [x for x in grid]  # add every line
    for i in range(9):
        column = [x[i] for x in grid]  # add every column
        grid_groups.append(column)
    for start_c, end_c in ((0, 3), (3, 6), (6, 9)):
        for start_l, end_l in ((0, 3), (3, 6), (6, 9)):
            square = []
            for line in grid[start_l:end_l]:
                for char in line[start_c:end_c]:
                    square.append(char)
            grid_groups.append(square)  # add every square
    for group in grid_groups:
        group_no_dots = [x for x in group if x != '.']
        if len(set(group_no_dots)) != len(group_no_dots):
            criterion = False
    return criterion


def sudoku2_2(grid):
    def unique(G):
        G = [x for x in G if x != '.']
        return len(set(G)) == len(G)
    def groups(A):
        B = zip(*A)
        for v in xrange(9):
            yield A[v]
            yield B[v]
            yield [A[v/3*3 + r][v%3*3 +c]
                   for r in xrange(3) for c in xrange(3)]

    return all(unique(grp) for grp in groups(grid))

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
print sudoku2(grid)

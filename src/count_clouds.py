from collections import deque
def fill_cloud1(grid, i, j):
    """
    Recursive implementation of the Flood Fill algorithm.
    """
    if i in range(len(grid)) and j in range(len(grid[0])) and grid[i][j] == '1':
        grid[i][j] = '0'
        print 'i={}, j={}'.format(i, j)
        for line in grid:
            print line
        fill_cloud1(grid, i - 1, j)
        fill_cloud1(grid, i + 1, j)
        fill_cloud1(grid, i, j - 1)
        fill_cloud1(grid, i, j + 1)


def countClouds1(skyMap):
    i, j, counter = 0, 0, 0
    for i in xrange(len(skyMap)):
        for j in xrange(len(skyMap[0])):
            if skyMap[i][j] == '1':
                counter += 1
                fill_cloud1(skyMap, i, j)
    print 'clouds:', counter
    return counter


def fill_cloud2(grid, i, j):
    """
    Forest Fire algorithm (Flood Fill with a queue.)
    """
    if grid[i][j] == '1':
        grid[i][j] = '2'
        queue = deque()
        queue.append((i, j))
        while len(queue) != 0:
            i, j = queue.popleft()
            print 'i, j', i, j
            if j + 1 < len(grid[0]) and grid[i][j + 1] == '1':
                grid[i][j + 1] = '2'
                queue.append((i, j + 1))
            if j - 1 >= 0 and grid[i][j - 1] == '1':
                grid[i][j - 1] = '2'
                queue.append((i, j - 1))
            if i + 1 < len(grid) and grid[i + 1][j] == '1':
                grid[i + 1][j] = '2'
                queue.append((i + 1, j))
            if i - 1 >= 0 and grid[i - 1][j] == '1':
                grid[i - 1][j] = '2'
                queue.append((i - 1, j))
            for line in grid:
                print line
            print queue
        return grid


def countClouds2(skyMap):
    counter = 0
    for i in xrange(len(skyMap)):
        for j in xrange(len(skyMap[0])):
            if skyMap[i][j] == '1':
                counter += 1
                fill_cloud2(skyMap, i, j)
    print 'clouds:', counter
    return counter


def fill_cloud3(grid, i, j):
    """
    Flood fill, going horizontally first, then north and south for each node.
    """
    pass



if __name__ == '__main__':
    grid = [
        ['1', '1', '1', '0'],
        ['1', '1', '0', '0'],
        ['1', '0', '0', '1'],
        ['1', '1', '0', '1'],
    ]
    countClouds2(grid)

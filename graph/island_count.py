grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]


def explore(grid, row, col, visited):
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])

    if not row_inbounds or not col_inbounds:
        return False

    if grid[row][col] == 'W':
        return False
    pos = (row, col)
    if pos in visited:
        return False
    visited.add(pos)
    #
    # queue = []
    # queue.append(grid[row][col])

    explore(grid, row, col - 1, visited)
    explore(grid, row, col + 1, visited)
    explore(grid, row - 1, col, visited)
    explore(grid, row + 1, col, visited)

    return True


def island_count(graph):
    count = 0
    visited = set()
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            print(grid[i][j], end=" ")
            if explore(graph, i, j, visited):
                count += 1

    print(count)


island_count(grid)

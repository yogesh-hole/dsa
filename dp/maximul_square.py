matrix = [["1", "1", "1", "1", "0"],
          ["1", "1", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]

matrix1 = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]]

matrix2 = [
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "0", "1", "1", "1", "1", "1",
     "1", "1", "1", "0", "0", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1",
     "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["0", "1", "1", "1", "1", "0", "1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "0", "1", "1",
     "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["0", "1", "0", "1", "1", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1",
     "1", "1", "1", "1", "1", "0", "1", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "0", "0",
     "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1",
     "1", "1", "1", "0", "1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1"],
    ["0", "1", "1", "0", "1", "1", "0", "1", "0", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1",
     "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1", "0", "1"],
    ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1", "1",
     "0", "0", "1", "1", "0", "0", "1", "1", "0", "1", "1", "0", "1", "0", "1", "0", "1"],
    ["1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0",
     "1", "1", "0", "1", "1", "1", "1", "0", "1", "0", "1", "1", "0", "1", "0", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1",
     "0", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1"],
    ["1", "1", "1", "0", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1",
     "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "0", "1", "1",
     "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1",
     "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1",
     "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1"],
    ["1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1", "0", "0", "1",
     "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0",
     "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0",
     "1", "1", "0", "0", "1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1",
     "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1"],
    ["1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1", "1", "1",
     "1", "0", "0", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1",
     "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0",
     "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1"],
    ["1", "1", "0", "0", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0",
     "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1",
     "0", "0", "1", "0", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "0", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0",
     "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "1", "1",
     "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1",
     "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1",
     "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1", "0",
     "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0",
     "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1"],
    ["1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
     "1", "1", "1", "0", "1", "1", "0", "0", "1", "1", "1", "0", "1", "1", "0", "1", "1"],
    ["1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "0", "1", "1",
     "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
     "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
     "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1",
     "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1"],
    ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "0", "1",
     "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1",
     "1", "0", "1", "0", "1", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
     "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1", "1"],
    ["1", "0", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
     "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1"],
    ["0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
     "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1",
     "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1",
     "1", "1", "1", "0", "1", "0", "1", "1", "0", "0", "1", "1", "1", "1", "0", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "1",
     "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0"],
    ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "1", "1",
     "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1"],
    ["1", "1", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1", "1", "1", "1", "0", "1", "1",
     "1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "0", "1", "0", "1", "0", "0"],
    ["0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1", "1", "1", "1", "1", "0", "0", "1", "0", "1",
     "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "0", "1"]]

matrix3 = [["1", "0", "1", "0", "0"],
           ["1", "0", "1", "1", "1"],
           ["1", "1", "1", "1", "1"],
           ["1", "0", "0", "1", "0"]]


def explore(matrix, row, col, visited, count):
    row_inbound = 0 <= row < len(matrix)
    col_inbound = 0 <= col < len(matrix[0])
    if not (row_inbound and col_inbound):
        return 0

    if matrix[row][col] == "0":
        return 0

    return 1 + min(
        explore(matrix, row, col + 1, visited, count),
        explore(matrix, row + 1, col, visited, count),
        explore(matrix, row + 1, col + 1, visited, count))


def find_max_square(matrix):
    max_square = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            max_square = max(max_square, explore(matrix, i, j, set(), 0))
    return max_square


def find_max_square_bottom_up(matrix):
    if matrix is None or len(matrix) < 1:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0]*(cols+1) for _ in range(rows+1)]
    max_square = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1":
                dp[i + 1][j + 1] = 1 + min(dp[i][j], dp[i][j + 1], dp[i + 1][j])
                max_square = max(max_square, dp[i+1][j+1])

    return max_square * max_square


# print(find_max_square(matrix))
# print(find_max_square(matrix1))
# print(find_max_square(matrix2))
print(find_max_square_bottom_up(matrix))
print(find_max_square_bottom_up(matrix2))
print(find_max_square_bottom_up(matrix3))

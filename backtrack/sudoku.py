def isValidSudoku(board):
    res = []
    for i in range(9):
        for j in range(9):
            element = board[i][j]
            if element != '.':
                res += [(i, element), (element, j), (i // 3, j // 3, element)]
    return len(res) == len(set(res))


def is_safe_number(board, row, col, num):
    for x in range(len(board[0])):
        if board[row][x] == num:
            return False

    for x in range(len(board)):
        if board[x][col] == num:
            return False

    for i in range(3):
        for j in range(3):
            start_row = row - row % 3
            start_col = col - col % 3
            if board[i + start_row][j + start_col] == num:
                return False
    return True


def solve_sudoku(board, row, col):
    if row == len(board) - 1 and col == len(board[0]):
        return True

    if col == len(board[0]):
        row += 1
        col = 0

    if board[row][col] != '.':
        return solve_sudoku(board, row, col + 1)

    for num in range(1, len(board) + 1):
        if is_safe_number(board, row, col, str(num)):
            board[row][col] = str(num)
            if solve_sudoku(board, row, col + 1):
                return True

        board[row][col] = '.'

    return False


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

# print(isValidSudoku(board))
if solve_sudoku(board, 0, 0):
    print(board)
else:
    print(False)

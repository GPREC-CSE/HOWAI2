def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve_n_queens_util(board, col):
        if col >= n:
            return True

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1

                if solve_n_queens_util(board, col + 1) == True:
                    return True

                board[i][col] = 0

        return False

    board = [[0]*n for _ in range(n)]

    if solve_n_queens_util(board, 0) == False:
        return "Solution does not exist"

    return board


def print_board(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
n = int(input("Enter the number of queens:"))
board = solve_n_queens(n)
if isinstance(board, str):
    print(board)
else:
    print_board(board)
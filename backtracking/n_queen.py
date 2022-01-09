#TODO: Revisit this later
N = 4

ld = [0] * 30

rd = [0] * 30

cl = [0] * 30

def print_sol(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print()

def solve_n_queen(board, col):
    if col >= N:
        return True

    for i in range(N):
        if ((ld[i - col + N - 1] != 1 and rd[i + col] != 1) and cl[i] != 1):
            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1

            if solve_n_queen(board, col + 1):
                return True

            board[i][col] = 0
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0

    return False

def solve_nq():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    if not solve_n_queen(board, 0):
        print("No Soln")
        return False

    return True

solve_nq()
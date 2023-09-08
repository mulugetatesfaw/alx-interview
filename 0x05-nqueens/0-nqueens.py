#!/usr/bin/python3
import sys

def nqueens(N):
    def is_safe(board, row, col):
        """Check if there is any queen in the same column"""
        for i in range(row):
            if board[i] == col:
                return False

        """Check if there is any queen in the same diagonal"""
        for i in range(row):
            if abs(board[i] - col) == abs(i - row):
                return False

        return True

    def solve(board, row):
        if row == N:
            # Print the solution
            print(','.join(str(col) for col in board))
        else:
            for col in range(N):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(board, row + 1)

    """Create an empty board"""
    board = [-1] * N

    """Start solving from the first row"""
    solve(board, 0)


if __name__ == '__main__':
    """Check the number of arguments"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    """Check the value of N """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    """Solve the N-queens problem"""
    nqueens(N)

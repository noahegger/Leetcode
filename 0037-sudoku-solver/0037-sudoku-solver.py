from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Initialize sets for rows, columns, and squares
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  # Key: (r//3, c//3)

        # Populate the sets based on the initial board state
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    squares[(r // 3, c // 3)].add(num)

        # Helper function to check if placing num is valid
        def isValid(row, col, num) -> bool:
            if (num in rows[row] or
                num in cols[col] or
                num in squares[(row // 3, col // 3)]):
                return False
            return True

        # Recursive backtracking function
        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for num in map(str, range(1, 10)):
                            if isValid(r, c, num):
                                # Place the number
                                board[r][c] = num
                                rows[r].add(num)
                                cols[c].add(num)
                                squares[(r // 3, c // 3)].add(num)

                                if solve():  # Recursively try to solve with this placement
                                    return True

                                # If it didn’t work out, reset (backtrack)
                                board[r][c] = "."
                                rows[r].remove(num)
                                cols[c].remove(num)
                                squares[(r // 3, c // 3)].remove(num)
                        return False  # If no number works here, backtrack
            return True

        solve()
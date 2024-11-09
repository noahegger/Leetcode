from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Initialize sets for rows, columns, and squares
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        full_set = set(map(str, range(1,10)))

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    square_r, square_c = r // 3, c // 3
                    squares[(square_r, square_c)].add(num)
        
        def valid_set(row, col) -> set:
            row_set = rows[row]
            col_set = cols[col]
            square_set = squares[(row//3,col//3)]
            return full_set.difference(row_set.union(col_set).union(square_set))

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for num in valid_set(r, c):
                            board[r][c] = num
                            rows[r].add(num)
                            cols[c].add(num)
                            squares[(r//3, c//3)].add(num)

                            if solve():
                                return True
                            board[r][c] = "."
                            rows[r].remove(num)
                            cols[c].remove(num)
                            squares[(r//3, c//3)].remove(num)
                        return False
            return True
        solve()
                            

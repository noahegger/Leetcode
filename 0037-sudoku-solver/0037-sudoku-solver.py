class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(board, r, c, num):
            # Check the row
            for i in range(9):
                if board[r][i] == num:
                    return False
            
            # Check the column
            for i in range(9):
                if board[i][c] == num:
                    return False
            
            # Check the 3x3 subgrid
            start_row, start_col = 3 * (r // 3), 3 * (c // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            
            return True

        def backtrack():
            # Find the next empty square
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        # Try placing each number from 1 to 9
                        for num in map(str, range(1, 10)):
                            if is_valid(board, r, c, num):
                                board[r][c] = num
                                if backtrack():
                                    return True
                                board[r][c] = "."
                        return False
            return True
            
        backtrack()
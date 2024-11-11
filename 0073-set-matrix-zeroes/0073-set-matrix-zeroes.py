class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])

        first_row_contains_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_contains_zero = any(matrix[i][0] == 0 for i in range(rows))

        # print(first_row_contains_zero)
        # print(first_col_contains_zero)

        # loop through matrix and set elements in first row and first column 
        # to zero (almost like a projection onto the boundary)
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # loop through rows and set to 0 if boundary is 0
        
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1,cols):
                    matrix[i][j] = 0
        
        # loop through cols and set to 0 if boundary is 0
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1,rows):
                    matrix[i][j] = 0

        # Need to zero out first row and first col
        # as thus far we would've only covered the [0][0] cell
        if first_row_contains_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
        if first_col_contains_zero:
            for i in range(rows):
                matrix[i][0] = 0
        
        
        


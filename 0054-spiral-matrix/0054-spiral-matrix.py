class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # n = len(matrix)
        # m = len(matrix[0])

        # matrix_list = []
        
        # start_row = 0
        # start_col = 0
        # end_row = n - 1
        # end_col = m - 1

        # while start_row <= end_row and start_col <= end_col:
        # #first row
        #     for j in range(start_col, end_col+1):
        #         matrix_list.append(matrix[start_row][j])
        #     start_row += 1
        # #last col
        #     for i in range(start_row, end_row+1):
        #         matrix_list.append(matrix[i][end_col])
        #     end_col -= 1
        # #last row
        #     if start_row <= end_row:
        #         for j in range(end_col, start_col-1, -1):
        #             matrix_list.append(matrix[end_row][j])
        #         end_row -= 1
        # #first col
        #     if start_col <= end_col:
        #         for i in range(end_row, start_row-1, -1):
        #             matrix_list.append(matrix[i][start_col])
        #         start_col += 1

        # return matrix_list

        # crazy brilliant solution
        # transpose, then reverse order of rows = 90 degree rotation
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = [*zip(*matrix)][::-1]
        
        return res




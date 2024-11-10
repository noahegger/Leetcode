class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) # num rows
        m = len(matrix[0]) # num cols

        def binary_search(row):
            #searches a row for mid col
            L, R = 0, m-1# first col, last col
            while L <= R:
                M = (L+R)//2
                if matrix[row][M] == target:
                    return True
                elif matrix[row][M] > target:
                    R = M - 1
                else:
                    L = M + 1
            return False
        
        T, B = 0, n-1 # first row, last row
        # search mid row
        while T <= B:
            M = (T+B)//2
            
            # check if first/last element of row is target
            if matrix[M][0] == target or matrix[M][m-1] == target:
                return True
            
            # Check if target is within range of row
            if matrix[M][0] < target < matrix[M][m-1]:
                return binary_search(M)
            
            # If target is less than first element, move up
            if target < matrix[M][0]:
                B = M - 1
            else:
                T = M + 1
        return False


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        # binary search approach

        def count_less_than_equal(x):
            count = 0
            j = n-1 #last column

            for i in range(n): #loop through each row
                while j>=0 and matrix[i][j] > x: # while element is > x, decrement column
                    j -= 1
                count += (j+1) #remaining # of columns to the left is how many are < x
            # after continuing through each row, count tells how many elements < x
            return count


        L = matrix[0][0]
        R = matrix[-1][-1]

        while L < R:
            M = (L+R)//2
            if count_less_than_equal(M) < k:
                L = M + 1
            else:
                R = M

        return L
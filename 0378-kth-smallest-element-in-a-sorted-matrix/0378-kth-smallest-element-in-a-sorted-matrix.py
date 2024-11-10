import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        # Binary search approach
        # def count_less_than_equal(x):
        #     count = 0
        #     j = n-1 #last column

        #     for i in range(n): #loop through each row
        #         while j>=0 and matrix[i][j] > x: # while element is > x, decrement column
        #             j -= 1
        #         count += (j+1) #remaining # of columns to the left is how many are < x
        #     # after continuing through each row, count tells how many elements < x
        #     return count

        # L = matrix[0][0]
        # R = matrix[-1][-1]

        # while L < R:
        #     M = (L+R)//2
        #     if count_less_than_equal(M) < k:
        #         L = M + 1
        #     else:
        #         R = M

        # return L

        # Min-Heap Approach
        min_heap = []
        for r in range(min(k, n)): #initialize heap with min number of rows needed
            heapq.heappush(min_heap, (matrix[r][0], r, 0)) #add first column of each row
        
        for _ in range(k):
            element, r, c = heapq.heappop(min_heap) 
            # remove the minimum element and push the subsequent column
            # if the column pushed is greater than an existing, we will automatically go to the next row
            if c+1 < n:
                heapq.heappush(min_heap, (matrix[r][c+1], r, c+1))
            # after k times, we will have kth smallest
        return element
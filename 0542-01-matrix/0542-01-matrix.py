from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows = len(mat)
        cols = len(mat[0])
        directions = [[0, 1],[0, -1], [1, 0], [-1,0]]
        distance = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        queue = deque()
     
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                    queue.append((i,j))

        while queue:
            r, c = queue.popleft()
            for dr,dc in directions:
                new_row = r+dr
                new_col = c+dc

                if 0<=new_row<rows and 0<=new_col<cols:
                    if distance[new_row][new_col] > distance[r][c] + 1:
                        distance[new_row][new_col] = distance[r][c]+1
                        queue.append((new_row, new_col))

        return distance
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # # First Idea #1 : DFS from each starting cell
        # # Redundant
        
        # rows, cols = len(heights), len(heights[0])
        # # Bordering
        # # Pacific = row = 0, col = 0
        # # Atlantic = row = m, col = n

        # dirs = [[0,1], [0, -1], [1, 0], [-1,0]]
        # def dfs(r, c):
        #     pac, atl = False, False
        #     seen = set()
        #     q = collections.deque()
        #     seen.add((r, c))
        #     q.append((r, c))

        #     while q:
        #         row, col = q.popleft()

        #         for dr, dc in dirs:
        #             r = row  + dr
        #             c = col + dc

        #             if (r in range(rows) and c in range(cols) and (r,c) not in seen and heights[r][c] <= heights[row][col]):
        #                 seen.add((r,c))
        #                 q.append((r,c))

        #             if r < 0 or c < 0:
        #                 pac = True
        #             if r == rows or c == cols:
        #                 atl = True

        #     return pac and atl


        # res = []
        # for r in range(rows):
        #     for c in range(cols):
        #         if dfs(r, c):
        #             res.append([r, c])
        
        # return res

        # Second Idea #2: Multi-Source DFS
        # Start from Pac/Atl borders and mark reachable cells
        # Return Intersection

        rows, cols = len(heights), len(heights[0])
        dirs = [[0, 1], [1,0], [0, -1], [-1,0]]

        pac_set = set()
        atl_set = set()

        def dfs(r, c, viable):
            viable.add((r, c))

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if (nr in range(rows) and nc in range(cols) and (nr,nc) not in viable and heights[nr][nc]>= heights[r][c]):
                    dfs(nr, nc, viable)
    
        # starting points
        for c in range(cols):
            dfs(0, c, pac_set) # top row
            dfs(rows-1, c, atl_set) # bottom row
        for r in range(rows):
            dfs(r, 0, pac_set)
            dfs(r, cols-1, atl_set)
        
        return list(pac_set & atl_set)


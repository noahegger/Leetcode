class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        
        # Bordering
        # Pacific = row = 0, col = 0
        # Atlantic = row = m, col = n

        dirs = [[0,1], [0, -1], [1, 0], [-1,0]]

        def dfs(r, c):
            pac, atl = False, False
            seen = set()
            q = collections.deque()
            seen.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    r = row  + dr
                    c = col + dc

                    if (r in range(rows) and c in range(cols) and (r,c) not in seen and heights[r][c] <= heights[row][col]):
                        seen.add((r,c))
                        q.append((r,c))

                    if r < 0 or c < 0:
                        pac = True
                    if r == rows or c == cols:
                        atl = True

            return pac and atl


        res = []
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c):
                    res.append([r, c])
        
        return res

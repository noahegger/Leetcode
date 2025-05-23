class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            dirs = [[-1, 0], [1,0], [0, -1], [0, 1]]

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    r = row + dr
                    c = col + dc
                    if (r in range(rows) and
                    c in range(cols) and 
                    grid[r][c] == "1" and
                    (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    bfs(r,c)
        return islands
        
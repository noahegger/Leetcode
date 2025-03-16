# Randumb thought:
# Invert the problem to loop through every unrotten orange
# and find the minimum adjacent distance to the nearest 
# rotten orange, keep track of the min
# minutes == steps

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: 
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        dirs = [[1,0], [-1,0], [0, 1], [0,-1]]

        def bfs(r,c):
            q = collections.deque()
            visited = set()
            q.append((r,c))
            visited.add((r,c))
            steps = 0

            while q:
                steps += 1
                for _ in range(len(q)): # This is a key part; without it, we can 
                # overcount if the first direction chosen is not the shortest
                # Otherwise stated, the existing queue needs to be processed on the same time footing
                    row, col = q.popleft()
                    for dr, dc in dirs:
                        r = row + dr
                        c = col + dc

                        if (r in range(rows) and
                        c in range(cols) and
                        (r,c) not in visited):
                            if grid[r][c] == 1:
                                q.append((r,c))
                                visited.add((r,c))
                            elif grid[r][c] == 0:
                                visited.add((r,c))
                            elif grid[r][c] == 2:
                                return steps
            return -1 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    min_steps = bfs(r,c)
                    if min_steps == -1:
                        return -1
                    minutes = max(minutes, min_steps)
        
        return minutes

        # Overall, inefficient, but the solution is intuitive. We end up revisiting cells often
        # After thought/alternative: Can we map cells to # of steps from rotten and store this information
        # in a grid? Minesweep type inference? Is there some mathematical structure?

        # Most popular solution is to queue rotten and count fresh. Then process directions, keep track of visited cells, 
        # and decrement fresh

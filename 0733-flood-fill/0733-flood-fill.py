class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        rows = len(image)
        cols = len(image[0])    
        seen = set()
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]

        def bfs(i, j, image):
            if (i < 0 or j <0 or i >= rows or j >= cols or (i,j) in seen):
                return

            seen.add((i,j))
            if image[i][j] == original:
                image[i][j] = color

                for dr, dc in directions:
                    # print(dr, dc)
                    bfs(i + dr, j+ dc, image)
        
        bfs(sr, sc, image)
        return image

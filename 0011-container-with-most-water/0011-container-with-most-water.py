class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(height)-1

        while l < r:
            if height[l] <= height[r]:
                area = height[l]*(r-l)
                l += 1
            else:
                area = height[r]*(r-l)
                r -= 1
            
            maxArea = max(maxArea, area)
        
        return maxArea



        



        area = min(h1, h2)*(idx2 - idx1)
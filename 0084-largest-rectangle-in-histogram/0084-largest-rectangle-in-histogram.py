class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        stack = []
        heights.append(0) # <- trick
      
        for idx in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[idx]:
                h = heights[stack.pop()]
                w = idx if not stack else idx - stack[-1] - 1
                area = h*w
                maxArea = max(maxArea, area)
            stack.append(idx)
        
        return maxArea
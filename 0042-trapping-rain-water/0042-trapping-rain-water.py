class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        total_water = 0

        for idx in range(len(height)):
            while stack and height[idx] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                width = idx - stack[-1] - 1
                h_bounded = min(height[idx], height[stack[-1]]) - height[top]
                total_water += h_bounded * width
            stack.append(idx)

        return total_water


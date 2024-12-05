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
        # two-pointer approach
        # left = 0
        # right = len(height) - 1
        # left_max = height[left]
        # right_max = height[right]
        # water = 0

        # while left < right:
        #     if left_max < right_max:
        #         left += 1
        #         left_max = max(left_max, height[left])
        #         water += left_max - height[left]
        #     else:
        #         right -= 1
        #         right_max = max(right_max, height[right])
        #         water += right_max - height[right]

        # return water

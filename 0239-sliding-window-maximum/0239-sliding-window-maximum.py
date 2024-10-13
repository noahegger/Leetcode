from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        d = deque()
        maxes = []

        # Store indices in the deque in decreasing order
        for idx, num in enumerate(nums):
            # print(d)
            # Hardest part I couldn't figure out: How do we track
            # the maximum element so we know when it falls out?
            if d and d[0] == idx - k:
                d.popleft()

            # Check if d is non-empty
            # If last item in d is less than current num, remove it
            while d and nums[d[-1]] < num: 
                d.pop()

            d.append(idx)

            # We don't start appending the maxes until
            # we've reached one full window
            # use d[0] as we ensure max is at the front
            if idx >= k-1:
                maxes.append(nums[d[0]])
            
        return maxes
            
            

        



            
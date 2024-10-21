class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen_map = {k:v for v,k in enumerate(nums)}
        
        #check if all are positive
        range = len(nums)+1 if all(k >= 0 for k in seen_map) else len(nums)
        i = 1
        while i <= range:
            if i not in seen_map:
                return i
            else:
                i+=1
        return
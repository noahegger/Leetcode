class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(start, temp):
            res.append(temp[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                temp.append(nums[i])
                backtrack(i+1, temp)
                temp.pop()
        nums.sort()
        backtrack(0, [])
        return res


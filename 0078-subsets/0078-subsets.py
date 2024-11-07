class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, temp = [], []

        def backtrack(i):
            if i == len(nums):
                res.append(temp[:])
                return

            # dont pick
            backtrack(i+1)

            # do pick
            temp.append(nums[i])
            backtrack(i+1)
            temp.pop()
            
        backtrack(0)
        return res
                

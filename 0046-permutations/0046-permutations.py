class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        remaining = [False]*n
        def backtrack(temp):
            if len(temp) == n:
                res.append(temp[:])
                return
            
            for i in range(n):
                if not remaining[i]:
                    temp.append(nums[i])
                    remaining[i] = True
                    backtrack(temp)
                    temp.pop()
                    remaining[i] = False
        backtrack([])
        return res
                



        
        backtrack(0)
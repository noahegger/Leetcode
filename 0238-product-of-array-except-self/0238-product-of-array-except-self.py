# I used 3 array initially
# Can I use only one?
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = 1
        suf = 1

        res = [1]*n

        for i in range(n):
            res[i] *= pre
            pre *= nums[i]

        for j in range(n):
            res[n-1-j] *= suf
            suf *= nums[n-j-1]
        
        return res
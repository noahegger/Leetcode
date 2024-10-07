# I used 3 arrays initially
# Can I use only one?
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        for i in range(1,n):
            res[i] = res[i-1]*nums[i-1]

        suf = nums[-1]
        for j in range(n-2, -1, -1):
            res[j] *= suf
            suf *= nums[j]
        
        return res
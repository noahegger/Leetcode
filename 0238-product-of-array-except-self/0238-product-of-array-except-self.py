class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        suf = [1]*n
        product = [1]*n
        for i in range(n):
            if i == 0:
                pre[i] = 1
                suf[n-i-1] = 1
            else:
                pre[i] = pre[i-1]*nums[i-1]
                suf[n-i-1] = nums[n-i]*suf[n-i]
            
        for i in range(n):
            product[i] = pre[i]*suf[i]
        return product
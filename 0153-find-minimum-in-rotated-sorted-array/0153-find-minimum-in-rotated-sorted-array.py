class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1

        if len(nums)== 1:
            return nums[0]

        while L <= R:
            M = (L+R)//2

            if nums[M] < nums[M-1]:
                return nums[M]
            if nums[M] > nums[M+1]:
                return nums[M+1]
            
            if nums[M] > nums[-1]:
                L = M
            else:
                R = M
        
        
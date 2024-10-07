# Compute max sum up to and including given endpoint
# If sum with endpoint[i] included is less than num[i] at that point,
# use num[i] as new sum
# Only update res (maximum sum) if the new max sum is greater
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            max_sum = max(max_sum+nums[i], nums[i])
            res = max(max_sum, res)
           
        return res

        
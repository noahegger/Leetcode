
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_thus = min_thus = result = nums[0]
        for num in nums[1:]:
            temp_max = max_thus
            max_thus = max(num, num * max_thus, num * min_thus)
            min_thus = min(num, num * temp_max, num * min_thus)
            result = max(result, max_thus)

        return result
            

            
        
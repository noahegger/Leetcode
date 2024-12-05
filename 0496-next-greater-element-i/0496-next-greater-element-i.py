class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hash_map = {}
            # {element in nums 2: next greatest element}
        stack = []
        output = []

        for num in nums2:
            while stack and num > stack[-1]:
                hash_map[stack.pop()] = num
            stack.append(num)
        
        for num in nums1:
            if num in hash_map:
                output.append(hash_map[num])
            else:
                output.append(-1)
        return output
            
            
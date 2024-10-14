class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        seen = {}        
        l = 0 

        print("String:", s)
        for r, char in enumerate(s):

            # if character has been seen before and it is after the current left index
            # move the left index forward after the repeat
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            
            # if char hasn't been seen, update max length comparing current
            # max to the right - left index
            else:
                max_length = max(max_length, r-l+1)
            
            seen[char] = r
        return max_length


            

            

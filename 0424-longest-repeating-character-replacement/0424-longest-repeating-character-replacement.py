class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        occurence_counter = {}
        l = r = 0
        max_count = 1
        max_len = 0

        while r < len(s):

            if s[r] not in occurence_counter:
                occurence_counter[s[r]] = 1
            else:
                occurence_counter[s[r]] += 1
                
            max_count = max(max_count, occurence_counter[s[r]])

            if (r-l +1) - max_count > k:
                occurence_counter[s[l]] -= 1
                l += 1
                

            max_len = max(max_len, r-l+1)
            r+=1

        return max_len


            

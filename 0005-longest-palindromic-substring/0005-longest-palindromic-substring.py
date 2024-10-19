class Solution:
    def expand_l_r(self, l_index: int, r_index: int, s:str) -> str:
        while l_index >= 0 and r_index < len(s) and s[l_index] == s[r_index]:
            l_index-=1
            r_index+=1
        return s[l_index+1:r_index]

    def longestPalindrome(self, s: str) -> str:
         
        res = ""
        for i in range(len(s)):
            #check odd palindrome
            palindrome_o = self.expand_l_r(i, i, s)
            if len(palindrome_o) > len(res):
                res = palindrome_o
            # check even palindrome
            palindrome_e = self.expand_l_r(i, i+1, s)
            if len(palindrome_e) > len(res):
                res = palindrome_e
        
        return res

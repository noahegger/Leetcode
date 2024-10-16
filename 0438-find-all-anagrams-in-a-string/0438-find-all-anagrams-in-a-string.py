class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sort_p = sorted(p)
        indices = []
        r = len(p)-1
        l = 0

        while r < len(s):
            if sorted(s[l:r+1]) == sort_p:
                indices.append(l)
            r += 1
            l += 1
        return indices

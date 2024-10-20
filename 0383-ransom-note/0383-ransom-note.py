class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
         
        magazine_map, ransom_map = {}, {}

        for c in magazine:
            if c not in magazine_map:
                magazine_map[c] = 1
            else:
                magazine_map[c] += 1


        for c in ransomNote:
            if c not in magazine:
                return False
            if magazine_map[c] == 0:
                return False
            else:
                magazine_map[c] -= 1
        return True
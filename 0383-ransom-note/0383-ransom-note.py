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
            if c not in ransom_map:
                ransom_map[c] = 1
            else:
                ransom_map[c] += 1
                if ransom_map[c] > magazine_map[c]:
                    return False
        return True
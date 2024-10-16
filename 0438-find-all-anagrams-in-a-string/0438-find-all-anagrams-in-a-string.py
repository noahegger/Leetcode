class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # First solution relying on sorted function
        # sort_p = sorted(p)
        # indices = []
        # r = len(p)-1
        # l = 0

        # while r < len(s):
        #     if sorted(s[l:r+1]) == sort_p:
        #         indices.append(l)
        #     r += 1
        #     l += 1
        # return indices

        # Second solution using hashmap to count frequencies

        count_map, p_map = {}, {}
        indices = []
        r = l = 0

        for char in p:
            if char not in p_map:
                p_map[char] = 1
            else:
                p_map[char] += 1

        while r < len(s):
            print(r)
            print(count_map)
            if s[r] not in count_map:
                count_map[s[r]] = 1
            else:
                count_map[s[r]] += 1

            if r - l + 1 > len(p):
                # print(r, l)
                count_map[s[l]] -= 1
                
                if count_map[s[l]] == 0:
                    count_map.pop(s[l])
                l += 1
            

            if count_map == p_map:
                indices.append(l)

            r += 1
        
        return indices

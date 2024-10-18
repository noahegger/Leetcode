class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check_condition(seen_map, t_map):
            for char, count in t_map.items():
                if char not in seen_map or seen_map[char] < t_map[char]:
                    return False
            return True

        # Start expanding right until all of t is in s
        # Once window is found, shrink from the left until condition no longer satisfied
        # continue expanding right
        # Return "" if condition never met

        if len(t) > len(s):
            return ""

        t_map = {}
        seen_map = {}
        for char in t:
            if char not in t_map:
                t_map[char] = 1
            else:
                t_map[char] += 1
        
        l = r = 0
        min_substring = ""
        min_indices = None
        while r < len(s):
            print(min_indices)
            if s[r] not in seen_map:
                seen_map[s[r]] = 1
            else:
                seen_map[s[r]] += 1
            
            condition = check_condition(seen_map, t_map)
            while condition:
                if min_indices is None or r-l+1 <= min_indices[1] - min_indices[0]:
                    min_indices = (l, r+1)

                seen_map[s[l]] -= 1
                l += 1
                condition = check_condition(seen_map, t_map)
            
            r+=1

        return "" if min_indices is None else s[min_indices[0]:min_indices[1]]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letter_map = {
            '2': ["a", "b", "c"],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res, temp = [], []

        def backtrack(i, temp):
            if len(temp) == len(digits):
                res.append(temp[:])
                return 

            curr = list(digits)[i]
            for c in letter_map[curr]:
                backtrack(i+1, temp+c)
            

        backtrack(0, "")
        return res


class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []

        char_map = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        }

        for char in s:
            if char == "(" or char == "{" or char == "[":
                self.stack.append(char)
            else:
                if not self.stack or char != char_map[self.stack[-1]]:
                    return False
                self.stack.pop()
        
        return not self.stack
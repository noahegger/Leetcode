class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []

        if len(s) < 2:
            return False

        char_map = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        }

        for char in s:
            if char == "(" or char == "{" or char == "[":
                self.stack.append(char)
            else:
                if len(self.stack) == 0:
                    return False
                if char != char_map[self.stack[-1]]:
                    return False
                else:
                    self.stack.pop()
        
        if len(self.stack) == 0:
            return True
        else:
            return False
        
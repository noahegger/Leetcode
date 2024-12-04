class Solution:
    def calculate(self, s: str) -> int:
        def rec(stack: list, s: str, index: int) -> int:
            num = 0
            sign = 1  # 1 means positive, -1 means negative
            while index < len(s):
                c = s[index]
                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == "+":
                    stack.append(sign * num)
                    num = 0
                    sign = 1
                elif c == "-":
                    stack.append(sign * num)
                    num = 0
                    sign = -1
                elif c == "(":
                    num, index = rec([], s, index + 1)
                    stack.append(sign * num)
                    num = 0
                elif c == ")":
                    stack.append(sign * num)
                    return sum(stack), index
                index += 1
            stack.append(sign * num)
            return sum(stack)

        return rec([], s, 0)

        

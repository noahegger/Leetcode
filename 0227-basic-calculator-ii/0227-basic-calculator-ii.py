class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        index = 0
        op = "+"
        while index < len(s):
            c = s[index]
            if c.isdigit():
                num = num * 10 + int(c)
            if c in "+-/*" or index == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop()*num)
                elif op== "/":
                    stack.append(int(stack.pop()/num))
                num = 0
                op = c
            index += 1
        
        return sum(stack)


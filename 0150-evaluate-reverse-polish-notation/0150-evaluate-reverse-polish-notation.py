class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in tokens:
            if x == "+":
                exp = int(stack.pop()) + int(stack.pop())
                stack.append(exp)
            elif x=="-":
                a = stack.pop()
                b = stack.pop()
                exp = int(b) - int(a)
                stack.append(exp)
            elif x == "/":
                a = stack.pop()
                b = stack.pop()
                exp = int(int(b) / int(a))
                stack.append(exp)
            elif x == "*":
                exp = int(stack.pop()) * int(stack.pop())
                stack.append(exp)
            else:
                stack.append(x)
        return int(stack[-1])
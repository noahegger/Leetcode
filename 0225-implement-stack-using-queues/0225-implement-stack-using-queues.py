from collections import deque
class MyStack:
    # Kind of a dumb question to use two queues in python
    # Given only deque exists (unless inefficient list)
    # and the deque is doubly sided, making this redundant
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        element = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return element
        
    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        element = self.q1.popleft()
        self.q2.append(element)
        self.q1, self.q2 = self.q2, self.q1

        return element

    def empty(self) -> bool:
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
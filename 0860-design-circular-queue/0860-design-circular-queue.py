class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = []
        self.max_size = k

    def enQueue(self, value: int) -> bool:
        if len(self.queue) == self.max_size:
            return False
        self.queue.append(value)
        return True
        
    def deQueue(self) -> bool:
        if len(self.queue) == 0:
            return False
        self.queue.pop(0)
        return True
    
    def Front(self) -> int:
        if not self.queue:
            return -1
        return self.queue[0]

    def Rear(self) -> int:
        if not self.queue:
            return -1
        return self.queue[-1]
        
    def isEmpty(self) -> bool:
        return len(self.queue) == 0
        
    def isFull(self) -> bool:
        return len(self.queue) == self.max_size
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
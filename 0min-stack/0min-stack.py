class MinStack:

    def __init__(self):
        self.topp = -1
        self.stack = []
        self.minimum = inf

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(self.minimum, val)
        self.topp+=1

    def pop(self) -> None:
        self.stack.pop()
        self.topp-=1
        if self.minimum not in self.stack and self.stack:
            self.minimum = min(self.stack)
        elif self.topp == -1:
            self.minimum = inf

    def top(self) -> int:
        return self.stack[self.topp]

    def getMin(self) -> int:
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
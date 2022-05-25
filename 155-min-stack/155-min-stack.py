class MinStack:

    def __init__(self):
        self.topp = -1
        self.stack = []

    def push(self, val: int) -> None:
        self.topp += 1
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.topp -= 1

    def top(self) -> int:
        return self.stack[self.topp]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
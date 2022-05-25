class MinStack:

    def __init__(self):
        self.topp = -1
        self.stack = []
        self.mini = 0

    def push(self, val: int) -> None:
        self.topp += 1
        self.stack.append(val)
        if val < self.mini:
            self.mini = val

    def pop(self) -> None:
        self.stack.pop()
        self.topp -= 1

    def top(self) -> int:
        return self.stack[self.topp]

    def getMin(self) -> int:
        if self.mini in self.stack:
            return self.mini
        else:
            return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
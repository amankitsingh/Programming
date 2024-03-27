### Answer 1 - using array
### TC - O(1), SC - O(N)
class BrowserHistory:

    def __init__(self, homepage: str):
        self.queue = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.queue = self.queue[:self.current+1] + [url]
        self.current+=1
        
    def back(self, steps: int) -> str:
        self.current = max(0, self.current-steps)
        return self.queue[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.queue)-1, self.current+steps)
        return self.queue[self.current]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

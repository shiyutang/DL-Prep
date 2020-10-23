class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.currentidx = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.currentidx + 1] + [url]
        self.currentidx = len(self.history) - 1

    def back(self, steps: int) -> str:
        if steps <= self.currentidx:
            self.currentidx = self.currentidx - steps
        else:
            self.currentidx = 0
        return self.history[self.currentidx]

    def forward(self, steps: int) -> str:
        if self.currentidx + steps < len(self.history):
            self.currentidx += steps
        else:
            self.currentidx = len(self.history) - 1
        return self.history[self.currentidx]

# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("leetcode.com")
obj.visit("google.com")
obj.visit("facebook.com")
obj.visit("upitube.com")
param_1 = obj.back(1)
param_2 = obj.back(1)
param_3 = obj.forward(1)
obj.visit("linkedin.com")
param_4 = obj.forward(2)
param_5 = obj.back(2)
param_6 = obj.back(7)
print(param_1,param_2,param_3,param_4,param_5,param_6)
# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
# [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

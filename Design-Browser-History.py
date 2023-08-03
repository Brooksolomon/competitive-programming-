class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack=[homepage]
        self.id=0
        

    def visit(self, url: str) -> None:
        self.stack=self.stack[:self.id+1]
        self.stack.append(url)
        self.id+=1
    def back(self, steps: int) -> str:
        if steps >=self.id:
            self.id = 0
            return self.stack[self.id]
        self.id = self.id-steps
        return self.stack[self.id]
        

    def forward(self, steps: int) -> str:
        if steps >= len(self.stack) -self.id - 1:
            self.id=len(self.stack) - 1
            return self.stack[self.id]
        self.id +=steps 
        return self.stack[self.id]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

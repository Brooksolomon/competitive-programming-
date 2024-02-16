class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.count = 0
        self.strings = [""] * n
    
    def insert(self, idKey: int, value: str) -> List[str]:
        self.strings[idKey-1] = value
        if idKey-1 > self.count:  
            return []
        while self.n > self.count and self.strings[self.count]:
            self.count+=1
        return self.strings[idKey-1:self.count]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

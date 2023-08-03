class StockSpanner:

    def __init__(self):
        self.stock=[]
        self.indexer=0

    def next(self, price: int) -> int:
        while self.stock:
            if self.stock[-1][0] <= price:
                self.stock.pop()
            else:
                x = (self.indexer) - (self.stock[-1][1])
                self.stock.append((price,self.indexer))
                self.indexer+=1
                return x
        if not self.stock:
            self.stock.append((price,self.indexer))
            self.indexer+=1
            return self.indexer
        x = (self.indexer) - (self.stock[-1][1])
        self.stock.append((price,self.indexer))
        self.indexer+=1
        return x
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

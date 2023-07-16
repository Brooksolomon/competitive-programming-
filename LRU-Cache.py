class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mydict=dict()
        self.stack = deque()

    def get(self, key: int) -> int:
        x =  self.mydict.get(key,-1)
        if x!=-1:
            self.stack.remove(key)
            self.stack.append(key)
        return x
        
        

    def put(self, key: int, value: int) -> None:
        x =  self.mydict.get(key,-1)
        if x!=-1:
            self.stack.remove(key)  
        elif len(self.mydict) == self.cap:
            self.mydict.pop(self.stack.popleft())
        self.mydict[key] = value  
        self.stack.append(key)


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

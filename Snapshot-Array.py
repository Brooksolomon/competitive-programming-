class SnapshotArray:

    def __init__(self, length: int):
        self.arr = {}
        self.ss = []
        self.check = 1
        

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val
        self.check = 1
        

    def snap(self) -> int:
        if self.check:
            self.ss.append({**self.arr})
        else:
            self.ss.append(self.ss[-1])
        self.check = 0
        return len(self.ss) - 1
    
        

    def get(self, index: int, snap_id: int) -> int:
        return self.ss[snap_id].get(index,0)
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

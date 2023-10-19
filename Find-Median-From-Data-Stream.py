class MedianFinder:

    def __init__(self):
        self.myarr = []

    def addNum(self, num: int) -> None:
        self.myarr.append(num)
        

    def findMedian(self) -> float:
        self.myarr.sort()
        n = len(self.myarr)
        if not self.myarr:return None 
        if len(self.myarr)%2 == 0:
            return (self.myarr[n//2-1]  + self.myarr[n//2])  /2
        else:
            return self.myarr[n//2]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

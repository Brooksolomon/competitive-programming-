class UndergroundSystem:

    def __init__(self):
        self.md = {}
        self.average = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.md[id] = (stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.md[id]
        time = t - startTime
        if (startStation,stationName) in self.average:
            self.average[(startStation,stationName)] =(self.average[(startStation,stationName)][0]+time,self.average[(startStation,stationName)][1]+1)
        else:
            self.average[(startStation,stationName)] = (time,1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.average[(startStation,endStation)]
        return total/count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

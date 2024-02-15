class FrequencyTracker:

    def __init__(self):
        self.track = {}
        self.count = {}
        

    def add(self, number: int) -> None:
        if number in self.track:
            self.count[self.track[number]] -=1
            self.track[number] += 1    
        else:
            self.track[number] = 1
        self.count[self.track[number]] =self.count.get(self.track[number],0) +1
        

    def deleteOne(self, number: int) -> None:
        if number in self.track:
            self.count[self.track[number]] -=1
            if self.track[number] ==1:
                self.track.pop(number)
            else:
                self.track[number]-=1
                self.count[self.track[number]] +=1
  
    def hasFrequency(self, frequency: int) -> bool:
        return self.count.get(frequency,0) > 0



        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

import numpy as np
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events =  sorted (events, key = lambda x:x[0])
        x = np.max(events)
        heap=[]
        heapify(heap)
        count=0
        l=0
        for i  in range(1,x+1):
            while l < len(events) and events[l][0] == i:
                heappush(heap,events[l][1])
                l+=1
            while heap and heap[0] < i:
                heappop(heap)
            if heap:
                heappop(heap)
                count+=1
        return count  

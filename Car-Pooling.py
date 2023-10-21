class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[2]) 
        m = trips[-1][2] + 1
        presum = [0] * m

        for i in range(len(trips)):
            presum[trips[i][2]]-=trips[i][0]
            presum[trips[i][1]]+=trips[i][0]
       
        for i in range(1,m):
            presum[i]+=presum[i-1]
            
        if capacity < max(presum):
            return False
        return True


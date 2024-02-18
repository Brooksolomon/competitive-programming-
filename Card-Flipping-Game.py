class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        similar = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                similar.add(fronts[i])
        mini = 2001
        for i in set(fronts+backs):
            if i not in similar:
                mini = min(mini,i)
        if mini ==2001:
            return 0
        else:
            return mini

                
        

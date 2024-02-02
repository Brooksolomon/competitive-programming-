class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)
        for i in t:
            if s.get(i,0) < t[i]:
                return i
        
        

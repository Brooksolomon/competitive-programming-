class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        f = {}
        l = {}
        for i,j in  matches:
            f[i] = f.get(i,0) + 1
            l[j] = l.get(j,0) + 1
        a = set(f).difference(set(l))
        b = [i for i in l if l[i]==1]
        return [sorted(a),sorted(b)]

        

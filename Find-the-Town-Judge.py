class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        df = defaultdict(int)
        nodes = set(range(1,n+1))
        for i,j in trust:
            df[j] += 1
            if i in nodes:
                nodes.remove(i)
        for i in nodes:
            if df[i] == n-1:
                return i
        return -1

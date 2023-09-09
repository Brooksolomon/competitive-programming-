class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.mydict = defaultdict(list)
        count = 0
        self.ans = len(queries) * [-1]
        chars=set()
        for a,b in equations:
            x = values[count]
            self.mydict[a].append((b,x))
            self.mydict[b].append((a,1/x))
            count+=1
            chars.add(a)
            chars.add(b)
        count  = 0
        for que in queries:
            if que[0] in chars and que[1] in chars:
                self.dfs(que[0],set(),1,que[1],count)
            count+=1
        return self.ans

    def dfs(self,x,visited,pro,q,c):
        if x in visited:
            return
        visited.add(x)
        if x == q:
            self.ans[c] = float(pro)
        for ana in self.mydict[x]:
            self.dfs(ana[0],visited,pro*ana[1],q,c)







         


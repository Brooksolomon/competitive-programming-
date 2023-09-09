class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        self.quiet=quiet
        self.mydict = defaultdict(list)
        for a,b in richer:
            self.mydict[b].append(a)

        self.ans = [i for i in range(len(self.quiet))]
        for o in range(len(self.ans)):
            self.dfs(o,set(),o)
        return self.ans
    def dfs(self,x,visited,ori):
        if x in visited :
            return 
        
        if self.quiet[x] < self.quiet[self.ans[ori]]:
            self.ans[ori] = x
        visited.add(x)
        for elem in self.mydict[x]:
            self.dfs(elem,visited,ori)

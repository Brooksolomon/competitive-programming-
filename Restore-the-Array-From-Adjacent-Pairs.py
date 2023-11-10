class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        self.myGraph = defaultdict(list)
        for i,j in adjacentPairs:
            self.myGraph[i].append(j)
            self.myGraph[j].append(i)
        self.visited=set()
        self.ans = []
        self.dfs(min(self.myGraph,key = lambda x : len(self.myGraph[x])))
        return self.ans
        
    def dfs(self,x): 
        self.visited.add(x)
        self.ans.append(x)
        for i in self.myGraph[x]:
            if i not in self.visited:
                self.dfs(i)
        return

        

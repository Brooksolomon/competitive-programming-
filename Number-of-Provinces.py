class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int: 
        n = len(isConnected)
        roads=defaultdict(set)  
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] and i!=j:
                    roads[i+1].add(j+1)
                    roads[j+1].add(i+1)
        allnums = set(range(1,n+1))
        visited=set()
        count=1
        def dfs(x):
            visited.add(x)
            if not roads[x].difference(visited):
                return
            
            for i in roads[x].difference(visited):
                dfs(i)
        dfs(1)
        while allnums.difference(visited):
            count+=1
            dfs(list(allnums.difference(visited))[0])

        return count
                    

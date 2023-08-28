class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent  = [i for i in range(n+1)]
        rank = [1 for i in range(n+1)]
        def find(x):
            cur = parent[x]
            while cur != parent[cur]:
                cur = parent[cur]
            return cur
        def union(x,y):
            par1 = find(x)
            par2 = find(y)

            if par1 ==  par2:return False 

            if rank[par1] > rank[par2]:
                rank[par1]+=rank[par2]
                parent[par2] = par1
            else:
                rank[par2]+=rank[par1]
                parent[par1] = par2
            return True 

        for a ,b in edges :
            if not union(a,b):
                return [a,b]

            


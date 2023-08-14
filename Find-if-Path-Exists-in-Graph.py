class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n==1 and not edges:
            return True
        md = defaultdict(set)
        for i,j in edges:
            md[i].add(j)
            md[j].add(i)
        visited=set()
        def graph(x,check):
            visited.add(x)
            if not md[x].difference(visited):
                return check
            if destination in md[x]:
                check = True
                return check
            for i in md[x].difference(visited):
                check = graph(i,check)
            return check 
        return graph(source,False)

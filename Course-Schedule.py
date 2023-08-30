class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mydict = defaultdict(set)
        
        for i , j in prerequisites:
            mydict[i].add(j)
        visited = [False] * numCourses
        global ans 
        ans  = True
        def dfs(node,axel):
            if visited[node]:
                return
            if axel[node]:
                global ans 
                ans = False
                return
            axel[node] = True 
            for x in mydict[node]:
                dfs(x,axel)
            axel[node] = False
            visited[node] = True 
        for i in range(numCourses):
            if mydict[i] and not visited[i]:
                dfs(i,[False ] * numCourses)

        return ans

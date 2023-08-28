class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n =  len(grid)
        visited = set()
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]] 
        def validity (x,y):
            return (x < 0 or y < 0 or x > n - 1 or y > n - 1 )
        
        def dfs (x,y):
            if validity(x,y) or grid[x][y] == 0 or (x,y) in visited :
                return
            visited.add((x,y))
            for a,b in direction:
                dfs(x+a,y+b)
        def bfs ():
            ans = 0
            queue = deque(visited)
            while queue:
                q = len(queue)
                for _ in range(q):
                    x,y = queue.popleft()
                    for a , b in direction:
                        cx , cy = x +a , y + b
                        if validity(cx,cy) or (cx,cy) in visited :
                            continue 
                        if grid[cx][cy]:
                            return ans 
                        
                        queue.append((cx,cy))
                        visited.add((cx,cy))
                ans+=1
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dfs(i,j)
                    res = bfs()
                    return res

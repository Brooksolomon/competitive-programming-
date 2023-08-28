class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        direction = [[1,0],[0,1],[-1,0],[0,-1]]

        def invalid(x,y):
            return x< 0 or y < 0 or x == m or y == n
        def dfs(x,y):
            if invalid(x,y) or grid[x][y] !='1':
                return 
            grid[x][y]  = '2' 
            for a , b in direction :
                dfs(x+a , y+b)
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count+=1
                    dfs(i,j)

        return count 
        

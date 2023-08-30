class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxi = 0
        direction = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(x,y):
            if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y]!=1:
                return
            cur_count[0] +=1
            grid[x][y]=2
            for a,b in direction:
                dfs(x+a,y+b)
        cur_count = [0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur_count[0] = 0
                dfs(i,j)
                maxi = max(maxi,cur_count[0])
        return maxi

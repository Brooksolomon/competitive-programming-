class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.direction = [[1,0],[0,1],[-1,0],[0,-1]]
        self.ans=False
        self.newg = [[0] * self.cols for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.newg[i][j]:
                    self.dfs(i,j,self.grid[i][j],None)
                    if self.ans:
                        return self.ans
        return self.ans
    def dfs(self,x,y,cons,prev):
        if x < 0 or y < 0 or x  == self.rows or y == self.cols or self.grid[x][y]!=cons or self.ans:
            return
        if self.newg[x][y]==1:
            self.ans=True
            return 
        self.newg[x][y] = 1
        for a,b in self.direction:
            a,b  = a+x  , b+y
            if prev !=(a,b):    
                self.dfs(a,b,cons,(x,y))
            
    

                

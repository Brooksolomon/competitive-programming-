class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxSum = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                maxSum = max(maxSum,grid[i-1][j-1] +
                                    grid[i-1][j] +
                                    grid[i-1][j+1]+
                                    grid[i][j]+
                                    grid[i+1][j-1]+
                                    grid[i+1][j]+
                                    grid[i+1][j+1]
                                    )
        return maxSum

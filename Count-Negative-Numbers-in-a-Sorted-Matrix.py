class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c = 0
        for i in grid:
            if i[-1] >= 0:continue
            left , right = 0 , len(i) - 1
            while left <=right:
                m = left + (right - left ) // 2
                if i[m] < 0:
                    right=m-1
                elif i[m] >= 0:
                    left = m + 1
                
            c+=(len(i) - left)
        return c

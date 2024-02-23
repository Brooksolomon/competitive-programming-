class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        md =defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                md[i+j].append(mat[i][j])
        ans=[]
        down = False
        for i in md:
            if down:
                ans+=md[i]
            else:
                ans+=md[i][::-1]
            down = not down
        return ans

                    
        
        

        

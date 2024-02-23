class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        import numpy
        def calc(x,y):
            total = 0
            count=0
            for i,j in [(0,0),(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                if  0<= x+i<len(img) and 0<= y+j<len(img[0]):
                    total+= img[x+i][y+j]
                    count+=1
            return total//count 
        ans = numpy.copy(img)   
        for i in range (len(img)):
            for j in range(len(img[0])):
                ans[i][j]=calc(i,j)
        return ans

        

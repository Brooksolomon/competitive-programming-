class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        initpix = image[sr][sc]
        def paint(x,y):
            if (x < 0) or (y < 0) or (x > len(image) - 1 ) or (y > len(image[0]) - 1):
                return
            if image[x][y]!=initpix or image[x][y] ==color:
                return 
            image[x][y] = color
            paint(x+1,y)
            paint(x-1,y)
            paint(x,y+1)
            paint(x,y-1)

        paint(sr,sc)
        return image 
                        
                    
                        

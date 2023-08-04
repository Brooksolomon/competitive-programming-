class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if len(heights) == 1:return 0
        new=[]
        heapify(new)
        br=0
        for i in range(len(heights)-1):
            if len(new) < ladders:
                if heights[i] > heights[i+1]:
                    i=i+1
                    continue
                else:
                    heappush(new,heights[i+1] - heights[i])
            else:
                if heights[i] > heights[i+1]:
                    i=i+1
                    continue
                else:
                    if ladders > 0 :
                        x = heappop(new)
                        if  x < heights[i+1] - heights[i]:
                            heappush(new,heights[i+1] - heights[i])
                            br+=x
                        
                        else:
                            heappush(new,x)
                            br+=heights[i+1] - heights[i]
                        if br > bricks:
                            break
                    else:
                        br+=heights[i+1] - heights[i]
                        print(br,bricks)
                        if br > bricks:
                            break
            i+=1
        return i

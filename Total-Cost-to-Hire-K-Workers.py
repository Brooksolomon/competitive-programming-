class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        myarr=[]
        left , right = 0 , len(costs) -1
        for left in range(candidates):
            heappush(myarr,(costs[left],left))
        for right in range(len(costs)-1,len(costs)-1 - candidates,-1):
            if right-1 < left:
                break
            heappush(myarr,(costs[right],right))
        total=0
        for i in range(k):
            x = heappop(myarr)
            total +=x[0]
            if x[1] <= left and left+1<right:
                left+=1
                heappush(myarr,(costs[left],left))
            elif x[1]>=right and right-1>left:
                right-=1
                heappush(myarr,(costs[right],right))
            
        return total



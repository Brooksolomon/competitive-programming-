class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        global res
        res = 0
        d = [0] * n
        def helper(i,r,d,c):
            global res
            if i == len(r):
                if any(x != 0  for x in  d):return
                res = max(res,c)
                return
            
            d[r[i][0]] -=1
            d[r[i][1]] +=1
            helper(i+1,r,d,c+1)
            d[r[i][0]] +=1
            d[r[i][1]] -=1
            helper(i+1,r,d,c)
        helper(0,requests,d,0)
        return res



                    

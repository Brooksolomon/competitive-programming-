class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1, n+1)]
        cc=[]
        def recur(i,c):
            if len(c) == k:
                cc.append(c[:])
                return 
            if i >= n: 
                 return 
            
            c.append(nums[i])
            recur(i+1,c)
            c.pop()

            recur(i+1,c)
        recur(0,[])
        return cc

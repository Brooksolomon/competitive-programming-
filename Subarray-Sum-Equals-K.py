class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps=[]
        d = {}
        s=0
        c=0
        for i in nums:
            s += i
            ps.append(s) 
        for i in ps:
            if i - k in d:
                c +=d[i-k]
            if i==k:
                c+=1
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return c

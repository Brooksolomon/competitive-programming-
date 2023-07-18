class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
            ans= []
            res =[]
            def helper(ss,idx):
                x = dict(Counter(ss))
                if x not in res:
                    ans.append(ss[:])
                    res.append(x)
                if len(ans) == (2**len(nums)):
                    return 
                
                for i in range(idx,len(nums)):
                    ss.append(nums[i])
                    helper(ss,i+1)
                    ss.pop()
                
            helper([],0)
            return ans 

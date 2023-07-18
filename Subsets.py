class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans= []

        def helper(ss,idx):
            ans.append(ss[:])
            if len(ans) == (2**len(nums)):
                return 
            
            for i in range(idx,len(nums)):
                ss.append(nums[i])
                helper(ss,i+1)
                ss.pop()
            
        helper([],0)
        return ans 

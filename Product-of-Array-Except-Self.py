class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixprod=[1] * len(nums)
        prefixprod[0] = nums[0]
        for i in range(1,len(nums)):
            prefixprod[i] = prefixprod[i-1] * nums[i] 
        print(prefixprod) 
        postprod = [1] * len(nums)
        postprod[-1]= nums[-1]
        for i in range(len(nums)-2,0,-1):
            postprod[i] = postprod[i+1] * nums[i]
        print(postprod)
        ans =[1] * len(nums)
        ans[0]=postprod[1]
        ans[-1]=prefixprod[-2]
        for i in range(1,len(nums)-1):
            ans[i] = prefixprod[i-1] * postprod[i+1]
        return ans

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        for i,e in enumerate(nums):
            nums[i] = (e,i)
        maxi=0
        stack=[]
        stack.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i][0] < stack[-1][0]:
                stack.append(nums[i])
        maxi=0
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1][0] <= nums[i][0]:
                maxi = max(maxi,nums[i][1] - stack[-1][1])
                stack.pop()
        return maxi
                

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int: 
        minlength= float('inf')
        n = len(nums)
        left = 0
        summer = 0
        for right in range(n):
            summer += nums[right]
            while summer>=target:
                minlength = min(minlength,right - left + 1)
                summer-=nums[left]
                left+=1
        if minlength == float('inf'):return 0
        else:return minlength


        

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        maxi = 0
        nums.sort()
        for i in range(1,len(nums)):
            maxi = max(nums[i] - nums[i-1],maxi)
        return maxi

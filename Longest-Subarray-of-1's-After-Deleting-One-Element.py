class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums)-1
        count = 0
        l = r =0
        window = {}
        while r <  len(nums):
            window[nums[r]] = window.get(nums[r],0) + 1
            if window.get(0,0) <2:
                count = max(count,r-l)
            r+=1
            while window.get(0,0) >1:
                window[nums[l]] -=1
                l+=1
        return count 

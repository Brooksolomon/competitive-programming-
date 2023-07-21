class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        left , right = 0 , len(nums) - 1 
        nums.sort()
        if nums[-1] == len(nums)-1:
            return len(nums)
        if nums[0]!=0:return 0
        while left <=right:
            m = left + (right - left) // 2

            if nums[m] < m:
                return m
            elif nums[m] == m:
                left=m+1
            else :
                right = m - 1
        return left

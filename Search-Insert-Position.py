class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0 ,len(nums) -1
        while left <=right:
            m = left + (right - left) // 2
            if nums[m] > target:
                right = m-1
            elif nums[m] < target:
                left = m+1
            else:
                return m
        return left

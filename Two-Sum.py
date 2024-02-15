class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = nums
        nums = sorted(t)
        l =  0
        r = len(nums) -1 
        while l < r:
            if nums[l] + nums[r] == target:return t.index(nums[l]),len(nums) - 1- t[::-1].index(nums[r])
            elif nums[l] + nums[r] > target:r-=1
            else:l+=1


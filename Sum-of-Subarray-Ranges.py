class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n - 1):
            maxi = nums[i]
            mini = nums[i]
            for j in range(i + 1, n):
                if nums[j] > maxi:
                    maxi = nums[j]
                elif nums[j] < mini:
                    mini = nums[j]
                res += maxi - mini
        return res

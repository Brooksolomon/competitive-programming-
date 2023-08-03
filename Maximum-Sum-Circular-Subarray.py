class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxi =mini = nums[0]
        curmaxi = curmini = 0
        summer=0
        for i in range(len(nums)):
            curmaxi = max(nums[i],curmaxi + nums[i])
            maxi=max(maxi,curmaxi)
            curmini = min(nums[i],curmini + nums[i])
            mini = min(mini,curmini)
            summer+=nums[i]

        if mini==summer:return maxi
        else:return max(maxi,summer-mini)

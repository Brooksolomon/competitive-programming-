class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        presum=0
        maxi = nums[0]
        mini = 0
        for i in nums:
            presum+=i
            if presum-mini > maxi:
                maxi = presum-mini
            if presum < mini:
                mini = presum
        return maxi

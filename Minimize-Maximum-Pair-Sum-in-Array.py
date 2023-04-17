class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        MAXI =nums[0] + nums[((int(len(nums)))-1)]
        for i in range(1,int(len(nums)/2)):
            if MAXI < nums[i] + nums[((int(len(nums)))-1)-i]:
                MAXI = nums[i] + nums[((int(len(nums)))-1)-i]
        return MAXI

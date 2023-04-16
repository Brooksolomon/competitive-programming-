class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = range(len(nums) -1)
        for i in n:
            for j in n:
                x = str(nums[j]) + str(nums[j+1])
                y = str(nums[j+1]) + str(nums[j])
                if int(x) < int(y):
                    nums[j],nums[j+1] = nums[j+1], nums[j]
        ans = "" 
        if nums[0] != 0:
            for i in range(len(nums)):
                ans += str(nums[i])
        else:
            ans += str(0)
        return ans

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = {}
        n = len(nums)
        for i in range(n):
            l = i+1
            r = n-1
            while l < r:
                if nums[i] + nums[l] + nums[r] >0:
                    r-=1
                elif nums[i] + nums[l] + nums[r] <0:
                    l+=1
                else:
                    ans[(nums[i],nums[l],nums[r])] = 1
                    l+=1
        return ans


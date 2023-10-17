class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue                                                   
            for j in range(i+1,len(nums) - 3+1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue 
                cur = target - nums[i] - nums[j]
                left = j+1
                right = len(nums) - 1 
                while left < right:
                    if nums[left] + nums[right] == cur:
                        ans.append([ nums[i] ,nums[j],nums[left],nums[right]])
                        left+=1
                        while left < right and nums[left-1] == nums[left]:
                            left+=1 
                    elif nums[left] + nums[right] > cur:
                        right-=1
                    else:
                        left+=1
        return ans



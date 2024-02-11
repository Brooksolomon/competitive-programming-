class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        check  = False
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            elif check:
                return False
            else:
                if i==0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
                check = True
        return True

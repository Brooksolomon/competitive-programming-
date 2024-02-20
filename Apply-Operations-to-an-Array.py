class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        z = 0
        ans =[]
        for i in range(len(nums)-1):
            if nums[i] ==nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0         
            if nums[i] ==0:
                z+=1
                continue
            ans.append(nums[i])
        ans.append(nums[-1])
        return ans+ [0] * z 

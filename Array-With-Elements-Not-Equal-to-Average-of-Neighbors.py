class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n= len(nums)
        for i in range(n):
            swaps = 0
            for j in range(1,n-1):
                if nums[j] == ((nums[j-1] + nums[j+1])/ 2):
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    swaps +=1
            if swaps == 0:
                break
                

        return nums

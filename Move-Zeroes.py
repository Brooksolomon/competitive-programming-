class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pointer=0
        cycler=0
        for i in range(len(nums)):
                if nums[pointer]!=0:
                    nums[pointer],nums[cycler] = nums[cycler],nums[pointer]
                    cycler+=1
                    pointer+=1
                else:pointer+=1

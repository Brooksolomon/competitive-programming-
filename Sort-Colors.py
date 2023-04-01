class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        numer=[]
        for i in range(3):
            for j in range(n):
                if i == nums[j]:
                    numer.append(nums[j])
        for i in range(n):
            nums[i]=numer[i

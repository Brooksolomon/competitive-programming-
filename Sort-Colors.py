class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = 3 * [0]
        for i in nums:
            count[i]+=1
        l = 0
        for i in range(len(count)):
            for j in range(count[i]):
                nums[l] = i
                l+=1
        

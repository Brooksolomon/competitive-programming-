class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x=len(nums)
        arr=[]
        for i in nums:
            counter=0
            for j in range(x):
                if nums[j] < i:
                    counter+=1
            arr.append(counter)
            
        return arr

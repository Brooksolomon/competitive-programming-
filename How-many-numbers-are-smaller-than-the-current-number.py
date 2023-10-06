class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        ans=[]
        for i in nums:
            ans.append(temp.index(i))
        return ans
        

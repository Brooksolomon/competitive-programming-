class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums=[int(x) for x in nums]
        nums.sort()
        nums.reverse()
        x=str(nums[k-1])
        
        return x

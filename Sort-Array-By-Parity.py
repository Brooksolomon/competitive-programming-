class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        x = [n for n in nums if n%2==0]
        y = [n for n in nums if n%2!=0]
        return x+y

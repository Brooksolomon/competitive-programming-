class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        md = Counter(nums)
        count = 0
        for i in md:
            count+=(md[i] * (md[i]-1)) //2
        return count
        

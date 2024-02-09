class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = []
        for k,e in c.items():
            if e > len(nums)//3:
                ans.append(k)
        return ans

        

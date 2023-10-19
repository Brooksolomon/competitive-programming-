class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = 0
        md = {0:1}
        count = 0
        for i in nums:
            presum+=i
            if md.get(presum-k,0):
                count +=md.get(presum-k,0)
            md[presum] = md.get(presum,0) + 1
        return count

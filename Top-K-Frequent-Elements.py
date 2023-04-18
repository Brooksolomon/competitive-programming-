class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        x = sorted(Counter(nums).items(),key= lambda x : x[1], reverse=True)
        for i in range(k):
            ans.append(x[i][0])
        return ans

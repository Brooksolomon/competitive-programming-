class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative = []
        positive = []
        for i in nums:
            if i >0:
                positive.append(i)
            else:
                negative.append(i)
        ans = []
        for i in range(len(negative)):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans
            

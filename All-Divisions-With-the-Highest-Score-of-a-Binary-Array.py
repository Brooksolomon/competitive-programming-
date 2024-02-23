class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        totalOnes = sum(nums)
        curOnes = 0
        ans = []
        maxTotal = 0
        for i in range(len(nums)+1):
            if (i-curOnes) + (totalOnes - curOnes) > maxTotal:
                maxTotal = (i-curOnes) + (totalOnes - curOnes)
                ans = [i]
            elif (i-curOnes) + (totalOnes - curOnes) == maxTotal:
                ans.append(i)
            if i ==len(nums):break
            curOnes += nums[i]

        return ans

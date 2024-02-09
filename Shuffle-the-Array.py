class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for l in range(n):
            ans.append(nums[l])
            ans.append(nums[n+l])
        return ans

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n= len(nums)
        if k == n:
            return sum(nums) / k
        
        window = sum(nums[:k])
        maxi = window / k
        for i in range(1,n-(k-1)):
            window = window - nums[i-1] + nums[i+k - 1]
            if window/k > maxi:
                maxi = window/k
        return maxi

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n=len(nums)
        nums.sort()
        og=nums.copy()
        for i in range(1,len(nums)):  #Prefix_sum
            nums[i]+=nums[i-1]
        ans=[]
        for i in range(len(queries)):
            total = 0
            j = bisect_left(og,queries[i])
            print(j)
            if j > 0:
                total = (j*queries[i]) - (2*nums[j - 1]) + (nums[-1]) - (n-j)*queries[i]
            else:
               total =  nums[-1] - (n* queries[i])
            ans.append(total)
        return  ans


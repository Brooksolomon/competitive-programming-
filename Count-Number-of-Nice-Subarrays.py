class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i] =0
            else:
                nums[i] =1
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
        count= 0 
        md = {0:1}
        for i in nums:
            if md.get(i-k,None):
                count+=md[i-k]
            md[i] = md.get(i,0) +1
        return count

                

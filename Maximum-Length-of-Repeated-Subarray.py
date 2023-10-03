class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = [chr(x+65) for x in nums1]
        nums1 = ''.join(nums1)
        temp=""
        maxi = 0
        for i in nums2:
            temp+=chr(i+65)

            if temp in nums1:
                maxi = max(maxi,len(temp))
            else:
                temp= temp[1:]
        return maxi


        

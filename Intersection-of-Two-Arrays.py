class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=set()
        x = [0] * (max(max(nums1),max(nums2)) + 1)
        for i in nums1:
            x[i] += 1
        for i in nums2:
            if x[i] >0:
                a.add(i)
        return a

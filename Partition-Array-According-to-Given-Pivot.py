class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        after = []
        count = 0
        for i in nums:
            if i < pivot:
                before.append(i)
            elif i > pivot:
                after.append(i)
            else:
                count+=1
        return before + ([pivot] * count) + after
        

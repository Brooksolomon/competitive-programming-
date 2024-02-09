class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        myDict = {}
        for index, element in enumerate(nums):
            myDict[element] = index
        for i,j in operations:
            curInd = myDict[i]
            nums[curInd] = j
            myDict.pop(i)
            myDict[j] = curInd
        return nums

        

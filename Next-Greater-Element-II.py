class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=nums[::-1]
        ans=[]
        for i in range(len(nums)-1,-1,-1):
            while stack:
                if nums[i] >= stack[-1]:
                    stack.pop()
                else:
                    ans.append(stack[-1])
                    break
            else:ans.append(-1)
            stack.append(nums[i])
        return ans[::-1]

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = defaultdict()
        dict[nums2[-1]] = -1
        stack = []
        stack.append(nums2[-1])
        for i in range(len(nums2)-2,-1,-1):
            while stack:
                if nums2[i] > stack[-1]:
                    stack.pop()
                else:
                    dict[nums2[i]]=stack[-1]
                    break
            else:dict[nums2[i]] = -1
            stack.append(nums2[i])
        ans=[]
        for i in nums1:
            ans.append(dict[i])
        return ans
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(node,arr):
            if arr:
                x = len(arr)//2
                node.val = arr[x]
                node.left = helper(TreeNode(), arr[:x])
                node.right = helper(TreeNode(),arr[x+1:])
                return node
        return helper(TreeNode(),nums)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        c =False
        def helper(node,sum):
            if not node:
                return
            sum+=node.val

            if sum==targetSum and (not node.left and not node.right):
                    nonlocal c
                    c =True
            

            helper(node.left,sum)
            helper(node.right,sum)
        helper(root,0)

        return c
            

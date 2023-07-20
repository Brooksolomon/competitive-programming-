# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(node):
            if not node:
                return
            
            return 1 + max(helper(node.left),helper(node.right))
            
           
        

        return helper(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def Dfs(node):
            if not node:
                return 
            
            node.left = Dfs(node.left)
            node.right =Dfs(node.right)

            if node.val < low:return node.right
            if node.val > high:return node.left

          

            return node
        return Dfs(root)

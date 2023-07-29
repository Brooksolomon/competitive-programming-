# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global count
        count = 0
        def dfs(node,pv):
            if not node:
                return 
            global count
            if node.val >= pv:count+=1

            dfs(node.left,max(node.val,pv))
            dfs(node.right,max(node.val,pv))
        dfs(root,float('-inf'))
        return count

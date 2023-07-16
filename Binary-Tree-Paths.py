# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans  = []
    
        def helper(node,temp):
            if not node:
                return
            if node.left == None and node.right == None:
                ans.append("".join(temp) + str(node.val))
                return 
            temp.append(str(node.val)+"->")
            helper(node.left,temp)
            helper(node.right,temp)
            temp.pop()
        
        helper(root,[])
        return ans
    

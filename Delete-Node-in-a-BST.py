# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def Dfs(node,x):
            if not node:
                return 
            
            if node.val == x:
                if not node.right and not node.left:
                   node =None 
                   return
                elif node.right and node.left:
                    c = node.right
                    while c.left:
                        c = c.left
                    node.val = c.val
                    node.right = Dfs(node.right,node.val)
                    
                    return node
                else:
                    if node.left:
                        node=node.left
                    else:
                        node=node.right
            elif x < node.val:
                node.left =Dfs(node.left,x)
            else:node.right = Dfs(node.right,x)
            return node
        
        
        return Dfs(root,key)

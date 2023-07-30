# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque()
        if root:
            queue.append(root)
            check = True
            while queue:
                n = len(queue)
                for _ in range(n):
                    node = queue.popleft()

                    if node.right and node.left and check:
                        queue.append(node.left)
                        queue.append(node.right)
                    elif node.left and check:
                        queue.append(node.left)
                        check = False
                    elif node.right :
                        return False
                    elif not node.right and not node.left:
                        check = False 
                        continue
                    elif not check:return False
                    else:
                        check = False

                    
            return True

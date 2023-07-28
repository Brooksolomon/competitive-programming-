# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans =[]
        queue = []
        if root:
            queue.append(root)
        while queue:
            n = len(queue)
            new = []
            for _ in range(n):
                node = queue.pop(0)
                new.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(new)
        return ans

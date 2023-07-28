# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = deque()
        if root:
            queue.append(root)
            ans.append(root.val)

        
        while queue:
            n = len(queue)
            maxi=float('-inf')
            for c in range(n):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    maxi = max(node.left.val,maxi)
                if node.right:
                    queue.append(node.right)
                    maxi = max(node.right.val,maxi)
            ans.append(maxi)
        return ans[:-1]

        

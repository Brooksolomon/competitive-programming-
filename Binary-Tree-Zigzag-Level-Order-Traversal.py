# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans =[]
        queue = deque()

        if root:
            queue.append(root)
            check = False
            while queue:
                check = not check
                n = len(queue)
                cur = []
                for _ in range(n):
                    node = queue.popleft()
                    cur.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if check:
                    ans.append(cur)
                else:
                    ans.append(cur[::-1])
            return ans

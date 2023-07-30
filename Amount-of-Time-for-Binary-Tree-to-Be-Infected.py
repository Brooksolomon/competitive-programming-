# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def converttograph(node,parent,graph):
            graph[node.val] = []

            if node.left:
                graph[node.val].append(node.left.val)
                converttograph(node.left,node,graph)
            if node.right:
                graph[node.val].append(node.right.val)
                converttograph(node.right,node,graph)
            if parent:
                graph[node.val].append(parent.val)

            return graph
        mygraph = converttograph(root,None,dict())

        infected = set([start])
        queue=[(start,0)]
        while queue:
            node,t = queue.pop(0)
            for x in mygraph[node]:
                if x not in infected:
                    queue.append((x,t+1))
                    infected.add(x)
        return t

            

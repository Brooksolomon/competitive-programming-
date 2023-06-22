# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        anslist = []
        while head:
            anslist.append(head.val)
            head=head.next
        ans  = len(anslist) * [0]
        stack = []
        for i in range(len(anslist)):
            while stack and anslist[stack[-1]] < anslist[i]:
                ans[stack.pop()] = anslist[i]
            stack.append(i)
        return ans

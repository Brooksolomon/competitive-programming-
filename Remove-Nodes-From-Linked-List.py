# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(cur):
            if cur == None:
                return None 
            cur.next = helper(cur.next)

            if cur.next and cur.val < cur.next.val:
                return cur.next

            return cur

        return helper(head)

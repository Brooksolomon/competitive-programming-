# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return None
        if head.next==None or head.next.next==None:
            return False
        slow =fast = head
        slow=slow.next
        fast=fast.next.next

        while slow.next!=None and fast.next!=None and  fast.next.next!=None and slow!=fast:
            slow=slow.next
            fast=fast.next.next
        if slow==fast:
            return True 

        return False     

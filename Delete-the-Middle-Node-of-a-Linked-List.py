# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None :
            return None
        if head.next==None:
            return None
        slow = fast = head
        fol = ListNode()
        fol.next= head
        while fast.next!=None and fast.next.next!=None:
            fol=fol.next
            slow=slow.next
            fast=fast.next.next
        if fast.next!=None:
            fol=fol.next
            slow=slow.next
        fol.next=fol.next.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head==None:
            return None
        if head.next==None:
            return head
        newhead=ListNode()
        sequal = newhead
        futurehead = ListNode()
        forward = futurehead
        cur = head
        while cur.next!=None:
            if cur.val >= x:
                new  = ListNode()
                new.val=cur.val
                forward.next = new
                forward=forward.next
            else:
                new  = ListNode()
                new.val=cur.val
                sequal.next = new
                sequal = sequal.next
            cur = cur.next
        
        if cur.val >= x:
                new  = ListNode()
                new.val=cur.val
                forward.next = new
                forward=forward.next
        else:
                new  = ListNode()
                new.val=cur.val
                sequal.next = new
                sequal = sequal.next
        sequal.next=futurehead.next
        return newhead.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        newhead = ListNode ()
        while cur != None:
            new=ListNode()#none
            new.val=cur.val#2
            new.next = newhead.next  #1
            newhead.next = new #2
            cur=cur.next 
        return newhead.next

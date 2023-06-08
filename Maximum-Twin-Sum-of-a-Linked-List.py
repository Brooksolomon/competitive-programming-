# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        newhead = ListNode ()
        while cur != None:
            new=ListNode()#none
            new.val=cur.val#2
            new.next = newhead.next  #1
            newhead.next = new #2
            cur=cur.next 
        head2=newhead.next
        x=head
        y=head2

        high = 0
        while x.next!=None:
            sumN = x.val + y.val
            if sumN > high:
                high=sumN
            x=x.next
            y=y.next
            
        return high

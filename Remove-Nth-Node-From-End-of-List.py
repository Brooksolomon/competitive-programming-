# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first=second=head
        x = 0
        while second.next !=None and x < n:
            second=second.next
            x+=1
        if first == second:
            return None
        while second.next!=None:
            second=second.next
            first=first.next
            x+=1
        
        if x+1 ==n:
                head=head.next
                return head
        if first.next !=None:
            first.next=first.next.next
        return head

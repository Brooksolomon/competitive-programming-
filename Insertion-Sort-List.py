# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        if head.next==None:
            return head

        newhead = ListNode()
        newhead.next  = head
        newtail  = head
        cur  = head.next


        while cur:
            if newtail.val <= cur.val:
                newtail = cur
                cur=cur.next
            else:
                newtail.next=cur.next
                new =  newhead
                while new.next.val < cur.val:
                    new=new.next
                cur.next=new.next
                new.next=cur
                cur=newtail.next
        return newhead.next

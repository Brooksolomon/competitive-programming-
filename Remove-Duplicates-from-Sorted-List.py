# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        if head==None:
            return None
        if head.next!=None:
            second = head.next
        else: return head


        if first.val == second.val and second.next !=None:
            first.next=second.next
            second=second.next

        while second.next!= None :
            if first.val == second.val:
                first.next=second.next
                second=second.next
            else:
                first=first.next
                second=second.next
        if first.val == second.val:
            first.next=second.next
            second=second.next
        return head

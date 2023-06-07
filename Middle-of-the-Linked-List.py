# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one = two = head
        while two.next!=None and two.next.next!=None:
            one=one.next
            two=two.next.next
        if two.next!=None:
            one=one.next
        return one

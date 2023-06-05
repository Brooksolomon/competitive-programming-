# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        newhead = ListNode ()
        while cur != None:
            new=ListNode()
            new.val=cur.val
            new.next = newhead.next
            newhead.next = new
            cur=cur.next
        r =newhead
        check =True

        while r!=None and head!=None :
            if r.next.val != head.val:
                check = False
                break
            r=r.next
            head=head.next

        return check

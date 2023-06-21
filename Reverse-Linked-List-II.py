# Definition for singly-linked list.
class ListNode:
         def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
            if head==None:
                return None
            if head.next==None or left==right:
                return head

            newhead=ListNode()
            sequal = newhead
            x=1
            cur = head
            while x != left:
                sequal.next = cur
                cur=cur.next
                sequal=sequal.next
                x+=1
            z=x
            while x!=right+1:
                new = ListNode()
                new.val=cur.val
                new.next=sequal.next
                sequal.next=new
                cur=cur.next
                x+=1
            while z!=right+1:
                sequal=sequal.next
                z+=1
            sequal.next=None
            if cur!=None:
                sequal.next=cur
                
            while cur!=None and cur.next!=None :
                sequal.next = cur
                cur=cur.next
                sequal=sequal.next

            return newhead.next

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
        if head.next != None:
            second = head.next
        else:
            return head
         
        while first.val == second.val and second.next!=None:
            x=first.val
            head = second.next
            while head!=None and head.val==x:
                head=head.next
            if head==None:
                return None
            first = head
            if head.next != None:
                second = head.next
            else: return head
             
        third = head
        if head.next!=None:
            first = head.next
        else:
            return head
        
        if first.next !=None:
            second = first.next
        else:
            if third.val == first.val:
                return None
            else:
                return head
        if second.next==None:
            if first.val == second.val:
                head.next=None
                return head
            else: return head
        
        while second.next!=None:
            print(third.val,first.val,second.val)
            if first.val==second.val:
                x=second.val 
                while second.next!=None and  x==second.next.val:
                    second = second.next 
                third.next=second.next
                if third.next !=None:
                    first = third.next
                else: return head
                if first.next!=None:
                    second = first.next
                else: return head

                if second.next==None:
                    if first.val==second.val:
                       third.next=None
            else :
                second=second.next
                first=first.next
                third=third.next
                if second.next==None:
                   if first.val==second.val:
                       third.next=None

          
        return head

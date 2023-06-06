# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None
        n=1 
        temps = head
        while temps.next!=None:
            n+=1
            temps=temps.next
        print(n)
        x=0
        switch = False
        
        k=k%n
        while x < k:
            first=head
            last = head
            if last.next !=None:
                last=last.next
            else: return head

            while last.next!=None:
                first=first.next
                last=last.next
            temp=head
            last.next=temp
            head = last
            first.next=None
            x+=1

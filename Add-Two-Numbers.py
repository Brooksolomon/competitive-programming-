# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None or l2== None:
            return None 
        one =l1
        two =l2

        sum1=sum2=0
        rate = 1
        while one!=None and one.next!=None:
            sum1+=one.val*rate
            one=one.next
            rate*=10
        sum1+=one.val*rate
        rate = 1
        while two!=None and two.next!=None:
            sum2+=two.val*rate
            two=two.next
            rate*=10
        sum2+=two.val*rate

        sum=sum1+sum2
        head=ListNode()
        if sum==0:
            return ListNode(0)
        while sum!=0:

            x=int((sum)%10) 
            sum=sum//10
            new = ListNode(x)
            cur = head
            while cur.next!=None:
                cur=cur.next
            cur.next=new 
        return head.next

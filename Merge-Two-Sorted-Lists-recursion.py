# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:return list2
        def merge(head1,head2,ans):
            if head1==None or head2==None:
                if head1!=None:
                    ans.next=head1
                elif head2!=None:
                    ans.next=head2

                return 

            if head1.val > head2.val:
                new=ListNode(head2.val)
                ans.next=new 
                ans=ans.next
                merge(head1,head2.next,ans)
            elif head1.val <= head2.val:
                new=ListNode(head1.val)
                ans.next=new 
                ans=ans.next
                merge(head1.next,head2,ans)

            


        ans=ListNode()
        merge(list1,list2,ans)
        return ans.next
        

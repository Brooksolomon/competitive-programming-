# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            one = list1
            two = list2

            if one == None and two == None:
                return None
            if one == None:
                return two
            if two == None:
                return one
            head = ListNode()
            while one!=None and two!=None:
                cur = head
                while cur.next != None:
                    cur = cur.next
                if one.val > two.val:
                    x=ListNode(two.val)
                    cur.next = x
                    two = two.next
                else:
                    x=ListNode(one.val)
                    cur.next = x
                    one = one.next
            if one!=None:
                while cur.next != None:
                    cur = cur.next
                cur.next=one
            elif two!=None:
                while cur.next != None:
                    cur = cur.next
                cur.next=two

            return head.next

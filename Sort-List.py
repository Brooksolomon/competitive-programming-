# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def middle(head):
            slow = fast = head
            while fast.next!=None and fast.next.next!=None:
                slow=slow.next
                fast=fast.next.next
            return slow
        def merge(left,right):
            h = t = ListNode()
            while left and right:
                if left.val < right.val:
                    t.next=left
                    left=left.next
                else:
                    t.next=right
                    right=right.next
                t = t.next
            if left:
                t.next = left
            if right:
                t.next = right
            return h.next        
        def helper(node):
            if not node or not node.next :
                    return node
            
            left=node
            right = middle(node)
            temp = right.next
            right.next =None
            right= temp

            left = helper(left)
            right = helper(right)

            return merge(left,right)
        return helper(head)

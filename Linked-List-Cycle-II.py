# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head or not head.next:
                        return None

            slow = fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    break

            if slow != fast:
                return None

            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
                
            return slow

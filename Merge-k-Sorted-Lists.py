# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        myarr=[]
        for i in lists:
            cur = i
            while cur:
                myarr.append(cur.val)
                cur=cur.next
        print(myarr)
        heapify(myarr)
        head=ListNode()
        cur = head
        while myarr:
            new = ListNode(heappop(myarr))
            cur.next = new
            cur=cur.next
        return head.next            

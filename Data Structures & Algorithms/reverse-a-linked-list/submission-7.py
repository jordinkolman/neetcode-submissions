# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        curr = head
        vals = []
        while curr.next:
            vals.append(curr.val)
            curr = curr.next
        
        head = curr
        
        for val in vals[::-1]:
            curr.next = ListNode()
            curr = curr.next
            curr.val = val

        
        return head
        

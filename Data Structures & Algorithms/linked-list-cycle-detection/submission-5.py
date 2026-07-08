# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        checked = []
        if not head:
            return False
        while head.next:
            if head.next in checked:
                return True
            checked.append(head)
            head = head.next
        return False
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast_cousor = head
        slow_cursor = head
        while fast_cousor.next and fast_cousor.next.next:
            fast_cousor = fast_cousor.next.next
            slow_cursor = slow_cursor.next
            if fast_cousor == slow_cursor:
                return True
        return False
        
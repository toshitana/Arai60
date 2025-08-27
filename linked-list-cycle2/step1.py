# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_cursor = head
        slow_cursor = head
        while fast_cursor.next and fast_cursor.next.next:
            if fast_cursor == slow_cursor:
                return fast_cursor
            fast_cursor = fast_cursor.next.next
            slow_cursor = slow_cursor.next
        return None

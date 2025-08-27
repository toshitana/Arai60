# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while True:
            if head in visited:
                return True
            elif head is None:
                return False
            visited.add(head)
            head = head.next

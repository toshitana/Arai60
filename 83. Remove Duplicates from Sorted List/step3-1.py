# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique_head = ListNode(val = head.val)
        unique_node = unique_head
        while not head.next is None:
            next_head = head.next
            if head.val == next_head.val:
                head = head.next
            elif head.val != next_head.val:
                head = head.next
                unique_node.next = ListNode(val = head.val)
                unique_node = unique_node.next
        return unique_head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique_sorted_linked_list = ListNode(head.val)
        node = unique_sorted_linked_list
        while not head.next is None:
            head_next = head.next
            if head.val == head_next.val:
                head = head.next
            elif head.val != head_next.val:
                head = head.next
                node.next = ListNode(head.val)
                node = node.next
        return unique_sorted_linked_list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique_sorted_linked_list = ListNode(head.val)

        while not head.next is None:
            if head == head.next:
                head = head.next
            elif head != head.next:
                unique_sorted_linked_list.next = ListNode(head.val)
                unique_sorted_linked_list = unique_sorted_linked_list.next
                head = head.next
        return unique_sorted_linked_list

# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n/2)
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_head = even #save to attach later

        while even is not None and even.next is not None: 
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return head

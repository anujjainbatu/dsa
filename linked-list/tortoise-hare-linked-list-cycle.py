# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# tortoise-hare O(n), O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True

        return False

# brute force O(n), O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr_node = head
        my_set = set()

        while curr_node is not None:
            if curr_node in my_set:
                return True
            my_set.add(curr_node)
            curr_node = curr_node.next

        return False

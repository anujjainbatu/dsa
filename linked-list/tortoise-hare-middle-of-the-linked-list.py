# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n/2) Tortoise-Hare Algorithm
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

# O(n)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        counter = 0
        hash_map = {}
        while curr_node is not None:
            counter += 1
            hash_map[counter] = curr_node
            curr_node = curr_node.next

        mid = counter//2 + 1

        return hash_map[mid]

# O(n+n/2)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        counter = 0
        while curr_node is not None:
            counter += 1
            curr_node = curr_node.next

        mid = counter//2
        curr_node = head

        for i in range(mid):
            curr_node = curr_node.next

        return curr_node

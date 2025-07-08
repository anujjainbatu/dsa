# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n), O(1), https://youtu.be/PvrxZaH_eZ4?si=E9G96cAKSdIBRlq4
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None

# O(n), O(n)
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

# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

        '''
        Copy the data from the next node into the current node, and delete
        the next node instead.
        Summary:
        1. You don’t need head here.
        2. You’re not really deleting node; you're overwriting it with the next
            node and deleting the next one.
        3. This works only because you're guaranteed:
        4. The node is not the tail
        5. All values are unique (so replacing value is OK)
        '''

# https://www.geeksforgeeks.org/problems/find-length-of-loop/1

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
# O(n), O(1)
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                count = 1
                curr = slow.next
                while curr != slow:
                    curr = curr.next
                    count += 1
                    
                return count
                
        return 0

# O(n), O(n)
class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        curr = head
        travel = 0
        my_dict = {}
        
        while curr is not None:
            if curr in my_dict:
                return travel - my_dict[curr]
                
            my_dict[curr] = travel
            travel += 1
            curr = curr.next
                
        return 0

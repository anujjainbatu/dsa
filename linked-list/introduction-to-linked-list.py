#https://www.geeksforgeeks.org/problems/introduction-to-linked-list/1

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
'''
class Solution:
    def constructLL(self, arr):
        n = len(arr)
        head = None
        
        for i in range(n):
            new_node = Node(arr[i])
            if head is None:
                head = new_node
            else:
                current = head
                while current.next is not None:
                    current = current.next
                current.next = new_node
                
        return head

"""
Time Complexity: O(n^2)
"""

#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
'''
class Solution:
    def constructLL(self, arr):
        n = len(arr)
        head = None
        tail = None
        
        for i in range(n):
            new_node = Node(arr[i])
            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node
                
        return head

"""
Time Complexity: O(n)
"""
            

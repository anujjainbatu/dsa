# https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/0

'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    def insertAtEnd(self, head, x):
        new_node = Node(x)
        if head == None:
            head = new_node
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        
        return head

# https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/0

'''
#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        count = 0
        current_node = head
        while current_node is not None:
            count += 1
            current_node = current_node.next
            
            
        return count
        
        '''
        visits 1st node, count 1
        visits 2nd, count 2
        ....
        visit nth, count n
        visit n+1, loops break
        '''

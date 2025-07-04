# https://www.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1


''' Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def searchKey(self, n, head, key):
        curr_node = head
        while curr_node:
            if curr_node.data == key:
                return True
            curr_node = curr_node.next
            
        return False

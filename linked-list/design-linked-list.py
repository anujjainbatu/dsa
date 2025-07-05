# https://leetcode.com/problems/design-linked-list/description/

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr_node = self.head
        counter = 0
        while curr_node is not None:
            if counter == index:
                return curr_node.val
            counter += 1
            curr_node = curr_node.next

        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head == None:
            # If list is empty, both head and tail become new_node
            self.head = new_node
            self.tail = new_node
        else:
            # List is not empty, append to tail
            self.tail.next = new_node
            self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        new_node = Node(val)
        curr_node = self.head
        prev_node = None
        counter = 0

        while curr_node is not None and counter < index:
            counter += 1
            prev_node = curr_node
            curr_node = curr_node.next
        
        if counter == index:
            new_node.next = curr_node
            prev_node.next = new_node
            # Update Tail if inserted at Last
            if curr_node is None:
                self.tail = new_node
        else:
            print("Node is not inserted. Index out of bound!")

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        if index == 0:
            to_delete = self.head
            self.head = to_delete.next
            del to_delete
            # Update tail if list becomes empty
            if self.head is None:
                self.tail = None
            return
            
        counter = 0
        curr_node = self.head
        prev_node = None
        while curr_node is not None and counter < index:
            counter += 1
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return #Index out of bound!

        prev_node.next = curr_node.next

        if curr_node == self.tail:
            #If last element is deleted
            self.tail = prev_node
            
        del curr_node

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

"""
Complexity
Operation | Time Complexity | Space Complexity
get(index)	O(n)	O(1)
addAtHead(val)	O(1)	O(1)
addAtTail(val)	O(1)	O(1)
addAtIndex(i, v)	O(n)	O(1)
deleteAtIndex(i)	O(n)	O(1)
"""


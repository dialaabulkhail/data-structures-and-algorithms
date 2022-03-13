
"""
This class is used as a form for creating new nodes within the linked list.
it has two arguments: value of the node, and the adress of next node.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


""""
This class is used as a form for creating a linked list out of nodes.
it has one argument: Head which is the first node of the linked list.
"""
class LinkedList:
    def __init__(self):
        self.head = None

    
    """
    insert is a method used to add new node with the value of argument(value) at the begining of the linked list.
    """
    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node


    """
    includes is a method that returns true if the value argument exists in a node in the list, and returns false if its not repeated.
    """
    def includes(self, value):
        current = self.head
        while(current):
            if current.value == value:
                return True
            else:
                current = current.next
        return  False

    
    """
    __str__ is a method that returns a string of the sequence of nodes as added to the linked list.
    """
    def __str__(self):
        output = ""
        if self.head is None:
            output = "Empty linked List"

        else:
            current = self.head
            while(current):
                output += f'{current.value} -> '
                current = current.next
            output += "NULL"

        return output
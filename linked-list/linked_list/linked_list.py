
"""
This class is used as a form for creating new nodes within the linked list.
it has two arguments: value of the node, and the adress of next node.
"""
from platform import node


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


    ############### Code challenge 6 ###############
    """
    Append method: appends the argument value to the end of the linked list
    """
    def append(self, value):
        current = self.head
        while(current):
            if current.next is None:
                current.next = Node(value)
                return self.__str__()
            else:
                current = current.next
            
        self.head = Node(value)
        return self.__str__()


    """
    insert_before method adds a new node with the value immediately before the first node that has the value specified
    """
    def insert_before(self, value, new_value):
        


        


if __name__ == "__main__":
    ll = LinkedList()
    values = [1,3,2,5,6]
    for i in values:
        ll.insert(i)
    # ll.insert_before(2,10)
    print(ll.insert_before(2,10))



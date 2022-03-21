
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
    insert_before method -> adds a new node with the value immediately before the first node that has the value specified
    """
    def insert_before(self, value, new_value):
        if self.includes(value):
            current = self.head
        
            previous = None
            while(current):
                if current.value == value:
                    node = Node(new_value)
                    node.next = current
                    if previous:
                        previous.next = node
                    
                    else:
                        self.head = node
                    return self.__str__()
                previous = current
                current = current.next
        
        else:
            return "Invalid value"



    """
    insert_after method -> adds a new node with the given new value immediately after the first node that has the value specified
    """
    def insert_after(self, value, new_value): 
        if self.includes(value):
            current = self.head

            while(current):
                if current.value == value:
                    node = Node(new_value)
                    node.next = current.next
                    current.next = node
                    return self.__str__()
                current = current.next

        else:
            return "Invalid value"      



    """
    This method returns the length of the linked list, which will be used in the kthFromEnd mehtod
    """
    def length(self):
        count_length = 0
        current = self.head
        
        while(current):
            count_length +=1 
            current = current.next
            
        return count_length



    """
    kthFromEnd method is used to return the node's value that is k places from the tail of the linked list.
    """                        
    def kthFromEnd(self, k):

        if k >= self.length():
            return "Value is out of range!"

        if k < 0:
            result = abs(k) -1
             
        else:
            result = k 

        current = self.head
        for i in range(result):
            current = current.next
        return current.value
            
             

    """
    zipLists method --> return a new list of merging two lists together, each node of each list points to the node that has its index of the other list
    """
    def zipLists(self, list1, list2):
        list1_current = list1.head
        list2_current = list2.head

        while list1_current is not None and list2_current is not None: 
            list1_next = list1_current.next
            list2_next = list2_current.next
            
            list2_current.next = list1_next
            list1_current.next = list2_current

            list1_current = list1_next
            list2_current = list2_next

        return self.__str__()


            
if __name__ == "__main__":
    ll = LinkedList()
    values = [12,33,50,45,100]
    for i in values:
        ll.insert(i)

    print(ll.length())
    print(ll.kthFromEnd(2))

### zipped lists
    list1 = LinkedList()
    list2 = LinkedList()

    list1.append(1)
    list1.append(2)
    list1.append(3)
    list2.append(10)
    list2.append(11)
    list2.append(12)

    print(list1)
    print(list2)
    print(list1.zipLists(list1 , list2 ))





class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    
    
    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node


    def includes(self, value):
        current = self.head
        while(current):
            if current.value == value:
                return True
            else:
                current = current.next
        return  False

    

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


if __name__ == "__main__":
    ll = LinkedList()
    diala = Node("Diala")
    hala = Node("Hala")
    jude = Node("jude")

    ll.insert(diala)
    ll.insert(hala)
    ll.insert(jude)

    print(ll)
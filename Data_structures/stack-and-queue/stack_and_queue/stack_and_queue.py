
class Node:
    """
    This class creates a new node with t a value and a pointer to next node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None



class Stack:
    """
    Stack class has a top property. It creates an empty Stack when instantiated.
    class methods:
        1. push() --> Adds a new node with value to the top of the stack with an O(1) Time performance.
        2. pop() --> Removes the node from the top of the stack, raise exception when called on empty stack.
        3. peek() --> Returns value of the node located at the top of the stack, raise exception when called on empty stack.
        4. is_empty() --> Returns boolean indicating whether or not the stack is empty.

    
    """
    def __init__(self):
        self.top = None


    
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
    


    def pop(self):
        if not self.top:  # or if self.top is None
            raise Exception("Empty stack")
        
        temp = self.top   
        self.top = self.top.next
        temp.next = None
        return temp.value



    def peek(self):
        if not self.top:
            raise Exception("Empty stack")
        
        return self.top.value



    def is_empty(self):   # returns true if stack is empty and false if its not
        #if not self.top:
            #return True
        #return False
        return self.top == None




class Queue:
    """
    Queue class has a front property. It creates an empty Queue when instantiated.
    class methods:
        1.enqueue() --> Adds a new node with value to the back of the queue with an O(1) Time performance.
        2. dequeue() --> Removes the node from the front of the queue, raise exception when called on empty queue
        3. peek() --> Returns value of the node located at the front of the queue, Raise exception when called on empty stack.
        4. is_empty() --> Returns boolean indicating whether or not the queue is empty.
    """
    def __init__(self):
        self.front = None
        self.rear = None


    
    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node

        self.rear.next = node
        self.rear = node



    def dequeue(self):
        if not self.front:
            raise Exception("Empty Queue")
        
        temp = self.front
        self.front = self.front.next
        temp.next = None

        return temp.value



    def peek(self):
        if not self.front:
            raise Exception("Empty Queue")
        
        return self.front.value



    def is_empty(self):  
        return self.front == None





if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    
    
    print(q.front.next.value)
    print(q.dequeue()) 
    print(q.dequeue()) 
    print(q.dequeue()) 



    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print(s.top.value)
    s.pop()
    print(s.top.value)


 




   
    





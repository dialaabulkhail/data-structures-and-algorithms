
class Node:
    """
    This class is used for creating a new node with a value and a pointer to the next node.
    """
    def __init__(self, value):
        self.value = value
        self.next = None



class Stack: 
    """
    This class is used for creating a stack with top pointer to its lastley added node.
    methods:
    - push() --> used to add nodes to the stack following the approach of first in last out.
    - pop() --> used to remove a node from the top of the stack.
    - peek() --> used to return the value of the top pointer of the stack.
    """
    def __init__(self):
        self.top = None



    def push(self, value):   
        node = Node(value)
        node.next = self.top
        self.top = node


    def pop(self):
        try:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        except:
            raise Exception("Empty stack")


    def peek(self):
        try:
            return self.top.value
        except:
            raise Exception("Empty stack")




class PseudoQueue:  
    """
    This class is going to utilize 2 Stack instances to create and manage the queue.
    methods:
    enqueue() --> used to push the nodes to the PseudoQueue with first in first out approach.
    dequeue() --> extracts a value from the PseudoQueue, using a first-in, first-out approach and returns the extracted value.
    """
    def __init__(self, stack):
        self.stack = stack   # regular stack first in last out
        self.new_stack = Stack()  # empty stack
        
    

    def enqueue(self, value):  
        self.stack.push(value)
       
      
     
    def dequeue(self):
        try:
            while self.stack.top is not None:  #[3->2->1->none]
                self.new_stack.push(self.stack.pop()) #[1->2->3]

            temp = self.new_stack.pop()  # popped value, the top of empty_stack "first in enqueue"
            return temp
    
        except:
            raise Exception("Empty Queue")
  


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class Stack:  # first in last out [1<-2-<-3<-4]
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



class PseudoQueue:  # s1 = stack 1 # s2 = stack 2 
    def __init__(self, s2):
        self.s1 = Stack()
        self.s2 = s2
    


    def enqueue(self, value):
        self.s2.push(value)

     

    def dequeue(self):
        try:
            while self.s2.top is not None:
                self.s1.push(self.s2.pop())

            popped = self.s1.pop()

            while self.s1.top is not None:
                self.s2.push(self.s1.pop())

            return popped

        except:
            raise Exception("Empty Queue")
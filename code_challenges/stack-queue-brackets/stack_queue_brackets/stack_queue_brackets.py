"""
Node class used to create new node with a value and a pointer to the next node
"""
from contextlib import closing


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
Stack class used to create a new stack with adding and removing functionalities, push() is used to add values/nodes to the stack, pop() is used to remove a node located at the top and returns the removed value of the stack.
"""
class Stack:
    def __init__(self):
        self.top = None

    
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top  = node


    def pop(self):
        if self.top is None:
            return "Empty stack"

        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value
        
    
"""
Validate_brackets function is used to return a boolean of whether the string argument consists of balanced/validate brackets
"""
def validate_brackets(string):    

    openning_brackets = ['[', '{', '(']
    closing_brackets = [']', '}', ')']
    map = dict(zip(openning_brackets, closing_brackets))   ## creates a dictionary of keys and values corresponding from open/close brackets,, the map[element] changes its value to the corresponding one
  
    stack = Stack()
  
    for i in string:        
        if i in openning_brackets:
            stack.push(map[i])     ## pushes the value not the key in dictionary "the closing brakcet"
        
        elif i in closing_brackets:
            if stack.top is not None and i == stack.top.value:    ## closing brakcet must equal the value pushed above
                stack.pop()            ## we pop out each bracket that has an opening and a closing
            else:
                return False
        
    if stack.top is None:       ## if each bracket found its closing, the stack will remain empty and thats where the brackets are valid
        return True

    else:
        return False






if __name__ == "__main__":
    s  =validate_brackets('()[[Extra Characters]]')
    print(s)
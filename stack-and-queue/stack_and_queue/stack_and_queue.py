
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
    


    def pop(self):
        if self.top is None:
            raise Exception("Empty stack")
        
        temp = self.top   # 4 -> 3 -> 2 -> 1     4 top == temp
        self.top = self.top.next
        temp.next = None
        return temp.value


    def peek(self):
        pass


    def is_empty(self):
        pass

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.pop())


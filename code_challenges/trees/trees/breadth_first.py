"""
Node class is used to create a new node in the tree
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None


    def is_empty(self):
        if self.front == None:
            return True
        return False


    def enqueue(self, node):
        newNode = node
        if self.is_empty():
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode


    def dequeue(self):
        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        else:
            return None


    def peek(self):
        if not self.is_empty():
            return self.front.value
        return None



"""
Binary Tree class is used to initialize a tree.
"""
class BinaryTree:
    def __init__(self):
        self.root = None

    """
    breadth_first method takes tree as an argument and returns list of all values in the tree, in the order they were encountered.
    the input tree is going to be traversed in breadth_first approach
    """

    @staticmethod
    def breadth_first(tree, node = None, array = None):
        q = Queue()
        if array is None:
            array = []
        if tree.root:
            q.enqueue(tree.root)

        while q.peek():
            node_front = q.dequeue()
            array.append(node_front.value)

            if node_front.left:
                q.enqueue(node_front.left)
            if node_front.right:
                q.enqueue(node_front.right)

        return array

    
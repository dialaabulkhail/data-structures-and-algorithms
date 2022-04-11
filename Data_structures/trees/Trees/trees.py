
"""
Node class is used to create a node with a value and a pointer to left and right childs.
"""
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 



"""
BinaryTree class is used to traverse nodes in three different orders, root is the parent node.
methods:
pre_order() --> starts from the root node then the left node followed by the right node.    (root -> left -> right)
in_order() --> starts from the left node, followed by the root then the right               (left -> root -> right)
post_order() --> start from the left then the right then the root.                          (left -> right -> root)

All of the methods return an array of the values ordered as required.
"""
class BinaryTree:
    def __init__(self):
        self.root = None


    
    def pre_order(self):
        node = self.root
        stack = []

        def _recursion(node):
            stack.append(node.value)
            
            if node.left:
                _recursion(node.left)

            if node.right:
                _recursion(node.right)

            return stack
        
        _recursion(node)
        return stack
    


    def in_order(self):
        node = self.root
        stack = []

        def _recursion(node):
            
            if node.left:
                _recursion(node.left)
               
            stack.append(node.value)

            if node.right:
                _recursion(node.right)

            return stack
        
        _recursion(node)
        return stack



    def post_order(self):
        node = self.root
        stack = []

        def _recursion(node):
            
            if node.left:
                _recursion(node.left)

            if node.right:
                _recursion(node.right)

            stack.append(node.value)

            return stack
        
        _recursion(node)
        return stack



def max_value(node): 
    
    if node is None:  
        return float('-inf') 

    maximum_value = node.value 
    left_value = max_value(node.left)  
    right_value = max_value(node.right)  

    if left_value > maximum_value: 
        maximum_value = left_value

    if right_value > maximum_value:  
        maximum_value = right_value  

    return maximum_value
     
                
            


"""
Binary search tree class is a sub-class of Binary Tree class, it is used to add nodes, and to check for existance of nodes.
methods:
Add(value) --> adds a new node with a value to the binary search tree, smaller values to the left and larger values to the right.
contains(value) --> returns a boolean to indicate wether the value exists in a tree or not.
"""
class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()



    def Add(self, value):
        node = Node(value)
        current = self.root

        if self.root is None:
            self.root = node

        while current:
            if node.value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    return 

            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    return
                


    def contains(self, value):
        node = self.root

        if self.root is None:
            raise Exception("The Tree is Empty")

        if type(value) is not int:
            raise Exception("Please provide an integer value")

        while node:
            if node.value == value:
                return True
            
            if node.value > value:
                node = node.left
            
            else:
                node = node.right
            
        return False



                


    
if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    x = BinaryTree()

    x.root = node1
    node1.left = node2
    node1.right = node3

    y = BinarySearchTree()
    # y.root = node1
    y.Add(6)
    y.Add(7)
    y.Add(19)
    y.Add(2)

    # print(y.contains(3))
    # print(y.contains(7))
    # print(y.contains(2))
    


    # print(y.pre_order())
    # node4 = Node(4)
    # node2.left = node4
   
    # print(x.pre_order())   # [1, 2, 3]   # [1, 2, 4, 3]
    # print(x.in_order())    # [2, 1, 3]
    # print(x.post_order())  # [2, 3, 1]
  

    # print(x.pre_order())

    # node9 = Node(9)
    # node2.left = node9
    # print(x.pre_order())
    # print(y.contains("cat"))


    node = Node(2)  
    node.left = Node(7)  
    node.right = Node(5)  
    node.left.right = Node(6)  
    node.left.right.left = Node(1)  
    node.left.right.right = Node(11)  
    node.right.right = Node(9)  
    node.right.right.left = Node(4)  
  
    print(max_value(node)) 

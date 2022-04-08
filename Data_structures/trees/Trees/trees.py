

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
            stack.append(node.value)

            if node.left:
                _recursion(node.left)

            if node.right:
                _recursion(node.right)

            return stack
        
        _recursion(node)
        return stack




    def post_order(self):
        pass


    
if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    x = BinaryTree()

    x.root = node1
    node1.left = node2
    node1.right = node3

    # node4 = Node(4)
    # node2.left = node4
   
    # print(x.pre_order())   # [1, 2, 3]   # [1, 2, 4, 3]
    print(x.in_order())    # [2, 1, 3]
    # print(x.post_order())  # [2, 3, 1]
  
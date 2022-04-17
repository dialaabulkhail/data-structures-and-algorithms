"""
Node class is used to create a new node in the tree
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



"""
Binary Tree class is used to initialize a tree.
"""
class BinaryTree:
    def __init__(self):
        self.root = None




"""
breadth_first function takes tree as an argument and returns list of all values in the tree, in the order they were encountered.
the input tree is going to be traversed in breadth_first approach
"""
def breadth_first(tree):
    node = tree.root
    stack = [node]
    values = []

    if stack is None:
        raise Exception("Empty tree")
    while stack:
        value = stack.pop(0)
        values.append(value.value)

        if value.left:
            stack.append(value.left)
        if value.right:
            stack.append(value.right)

    return values
        


 
if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.right.right = Node(9)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right.left = Node(4)

    print(breadth_first(tree))


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 



class BinaryTree:
    def __init__(self):
        self.root = None



class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()
    

    """
    This method returns the summation of odd values in a binary search tree
    """
    def summ(self):
        node = self.root
        stack = []


        def _rec(node):
            if type(node.value) is int:
                if node.value % 2:
                    stack.append(node.value)
                
            if node.left:
                _rec(node.left)
            
            if node.right:
                _rec(node.right)
        

            return sum(stack)
        return _rec(node)
            



if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node("cat")
    node6 = Node(6)
    node7 = Node(7)


    y = BinarySearchTree()
    y.root = node1
    node1.left = node3
    node1.right = node2
    node2.left = node5
    node2.right = node4
    node3.left = node7
    node3.right = node6
    
    print(y.summ())
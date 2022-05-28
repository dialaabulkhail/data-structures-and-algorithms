class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 



class Tree:
    def __init__(self):
        self.root = None




def mirror_tree(t1, t2):
    node1 = t1.root
    node2 = t2.root

    def _traverse(node1, node2):
        if node1.value == node2.value:
            return True

        if node1.left and node2.right:
            _traverse(node1.left, node2.right)

        if node1.right and node2.left:
            _traverse(node1.right, node2.left)

        
        return False

    return _traverse(node1, node2)


if __name__ == "__main__":
    t1 = Tree()
    t2 = Tree()

    node1 = Node(2)
    node2 = Node(3)
    node3 = Node("hi")
    node4 = Node(0)
    node5 =Node(55)

    node11 = Node(2)
    node22 = Node("hi")
    node33 = Node(4)
    node44 = Node(55)
    node55 =Node(0)

    t1.root = node1
    t2.root = node11
    node1.left = node2
    node1.right = node3

    node11.left = node22
    node11.right = node33

    node2.left = node4
    node2.right = node5

    node33.left = node44
    node33.right = node55

    print(mirror_tree(t1,t2))


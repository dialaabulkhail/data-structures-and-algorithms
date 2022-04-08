from Trees.trees import BinaryTree, Node

                                            ######### Pre Order Binary trees tests #########

def test_pre_order():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    binary = BinaryTree()

    binary.root = node1
    node1.left = node2
    node1.right = node3

    assert [1, 2, 3] == binary.pre_order()
    assert 1 == binary.root.value
  

def test_adding_nodes_pre_order():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    binary = BinaryTree()

    binary.root = node1
    node1.left = node2
    node1.right = node3

    node7 = Node(7)
    node3.left = node7
    assert [1, 2, 3, 7] == binary.pre_order()

    node5 = Node("cat")
    node2.left = node5
    assert [1, 2, "cat", 3, 7] == binary.pre_order()

    node8 = Node("*")
    node7.right = node8
    assert [1, 2, "cat", 3, 7, "*"] == binary.pre_order()

#           1
#     2           3
# "cat"         7
#                 "*"


                                            ######### In Order Binary trees tests #########

def test_in_order():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    binary = BinaryTree()

    binary.root = node1
    node1.left = node2
    node1.right = node3

    assert [2, 1, 3] == binary.in_order()
    assert 1 == binary.root.value



def test_adding_nodes_in_order():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    binary = BinaryTree()

    binary.root = node1
    node1.left = node2
    node1.right = node3

    node7 = Node(7)
    node3.left = node7
    assert [2, 1, 7, 3] == binary.in_order()  

    node5 = Node("cat")
    node2.left = node5
    assert ["cat", 2, 1, 7, 3] == binary.in_order()   

    node8 = Node("*")
    node7.right = node8
    assert ["cat", 2, 1, 7, "*", 3] == binary.in_order()



                                            ######### Post Order Binary trees tests #########

def test_post_order():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    binary = BinaryTree()

    binary.root = node1
    node1.left = node2
    node1.right = node3

    assert [2, 3, 1] == binary.post_order()
    assert 1 == binary.root.value
  

def test_adding_nodes_post_order():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    binary = BinaryTree()

    binary.root = node1
    node1.left = node2
    node1.right = node3

    node7 = Node(7)
    node3.left = node7
    assert [2, 7, 3, 1] == binary.post_order()

    node5 = Node("cat")
    node2.left = node5
    assert ["cat", 2, 7, 3, 1] == binary.post_order()

    node8 = Node("*")
    node7.right = node8
    assert ["cat", 2, "*", 7, 3, 1] == binary.post_order()
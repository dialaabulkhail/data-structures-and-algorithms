
from Trees.trees import BinaryTree, Node


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





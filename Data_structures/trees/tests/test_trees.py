from Trees.trees import BinaryTree, Node, BinarySearchTree
import pytest

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



                                            ######### Add method Binary search tree tests #########

def test_Add():
    bst = BinarySearchTree()
    bst.Add(1)
    bst.Add(2)
    bst.Add(3)
    assert 1 == bst.root.value
    assert [1, 2, 3] == bst.pre_order()


def test_Add_orders(bst):
    assert [9, 5, 4, 8, 10] == bst.pre_order()
    assert [4, 5, 8, 9, 10] == bst.in_order()
    assert [4, 8, 5, 10, 9] == bst.post_order()



                                            ######### Contains method Binary search tree tests #########

def test_contains(bst):
    assert True == bst.contains(5)
    assert True == bst.contains(9)
    assert True == bst.contains(4)
    assert True == bst.contains(8)
    assert True == bst.contains(10)


def test_doesnt_contain(bst):
    assert False == bst.contains(7)
    assert False == bst.contains(199)
    assert False == bst.contains(54)
    assert False == bst.contains(0000)


def test_empty_tree():
    bst = BinarySearchTree()
    with pytest.raises(Exception):
        bst.contains()


def test_wrong_value(bst):
    with pytest.raises(Exception):
        bst.contains("string")
    


                                            ######### Fixtures #########

@pytest.fixture
def bst():
    bst = BinarySearchTree()
    bst.Add(9)
    bst.Add(5)
    bst.Add(4)
    bst.Add(8)
    bst.Add(10)

    return bst

#           9
#     5           10   
# 4      8

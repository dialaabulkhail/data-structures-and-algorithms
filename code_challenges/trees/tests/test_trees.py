from trees.breadth_first import Node, BinaryTree, breadth_first
import pytest



def test_breadth_first_empty():
    tree = BinaryTree()
    with pytest.raises(Exception):
        breadth_first(tree)



def test_breadth_first_single_element():
    tree = BinaryTree()
    tree.root = Node(8)
    assert breadth_first(tree) == [8]



def test_lab_values():
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
    assert [2,7,5,2,6,9,5,11,4] == breadth_first(tree)



def test_breadth_first_value_types():
    tree = BinaryTree()
    tree.root = Node(5)
    tree.root.left = Node("a")
    tree.root.right = Node(False)
    assert breadth_first(tree) == [5, "a", False]

    tree.root.left.left = Node(100)
    tree.root.left.right = Node("cat")
    tree.root.right.right = Node(8)
    tree.root.left.left.left = Node(-0.56)
    tree.root.left.left.right = Node(True)
    tree.root.right.right.right = Node("fun")
    tree.root.right.right.right.left = Node([7, 7])
    assert breadth_first(tree) == [5, "a", False, 100,"cat", 8, -0.56, True, "fun", [7,7]]
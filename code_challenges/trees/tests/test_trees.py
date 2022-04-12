from trees.breadth_first import Node, BinaryTree

def test_breadth_first_binarytree_empty():
    tree = BinaryTree()
    assert BinaryTree.breadth_first(tree) == []


def test_breadth_first_binarytree_one_element():
    tree = BinaryTree()
    tree.root = Node(8)
    assert BinaryTree.breadth_first(tree) == [8]


def test_breadth_first_binarytree_with_letters():
    tree = BinaryTree()
    tree.root = Node(8)
    tree.root.left = Node("a")
    tree.root.right = Node(-2)
    assert BinaryTree.breadth_first(tree) == [8, "a", -2]
    tree.root.left.left = Node(195)
    tree.root.left.right = Node("cat")
    tree.root.right.right = Node(8)
    tree.root.left.left.left = Node(-0.56)
    tree.root.left.left.right = Node(9)
    tree.root.right.right.right = Node(23)
    tree.root.right.right.right.left = Node([5, 7])
    assert BinaryTree.breadth_first(tree) == [8, "a", -2, 195,"cat", 8, -0.56, 9, 23, [5,7]]
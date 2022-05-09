from trees.breadth_first import BinaryTree, Node, breadth_first
from trees.fizzbuzz import fizzbuzz_tree


def test_fizzbuzz():
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

    assert ['2', '7', 'Buzz', '2', 'Fizz', 'Fizz', 'Buzz', '11', '4'] == fizzbuzz_tree(breadth_first)
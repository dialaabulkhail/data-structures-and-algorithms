from trees.breadth_first import breadth_first, Node, BinaryTree 

def fizzbuzz_tree(breadth_first):
    breadth_first_tree = breadth_first(tree)
    result = ["Fizz"*(not i%3) + "Buzz"*(not i%5) or f"{i}" for i in breadth_first_tree]
    return result


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
    tree.root.right.right.left.right = Node(15)

    print(breadth_first(tree))
    print(fizzbuzz_tree(breadth_first))
# Trees
Trees are a type of data structures that consists of a root node, which is always pointing to left and/or right nodes in case it was a tree of a type (Binary), otherwise, if the root is pointing to more than two nodes, its then of type  (K=ary).
heigth of a tree is reffered to the number of edges amongst the tree, while an edge itself means the links between each node and its pointer node. Finally, a leaf represents the last child node in the tree.


## Challenge
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

Create a Binary Tree class:
Define a method for each of the depth first traversals:
1. pre order
2. in order
3. post order which returns an array of the values, ordered appropriately.

Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.


Binary Search Tree:
Create a Binary Search Tree class

This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
1. Add
- Arguments: value
- Return: nothing
- Adds a new node with that value in the correct location in the binary search tree.
- Contains
- Argument: value
- Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## API
1. Class node:
initializes a node with a value and a pointer to left and right nodes.

2. Class BinaryTree:
- creates a root node
- pre_order() --> returns an array of values starting from the root node then the left node followed by the right node. 
- in_order() --> returns an array of values starting from the left node, followed by the root then the right.
- post_order() --> returns an array of values starting from the left then the right then the root.


3. Class BinarySearchTree:

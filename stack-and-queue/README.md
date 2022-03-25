# Stacks and Queues
A Stack is a type of data structure that stores nodes with each one pointing at the next node, the pointer which we can control in the stack is the (Top) which always points at the last node added.
- First in last out.

![](./stacks-queue/stack.jpg)

A Queue is a linear type of data structures that stores nodes in which the front one refers to the rear one
- first in first out
-last in last out

![](./stacks-queue/queue.png)


## Challenge
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
- Create a Stack class that has a top property. It creates an empty Stack when instantiated.
- Create a Queue class that has a front property. It creates an empty Queue when instantiated.


## Approach & Efficiency

Stack time complexity --> O(1)

Stack space complexity --> O(1)


## API
1. push() --> 
- adds a new node with that value to the top of the stack with an O(1) Time performance.

2. pop () --> 
- Returns: the value from node from the top of the stack.
- Removes the node from the top of the stack.
- Should raise exception when called on empty stack.

3. peek() --> 
- Returns: Value of the node located at the top of the stack.
- Should raise exception when called on empty stack.

4. is_empty() -->
- Returns: Boolean indicating whether or not the stack is empty.

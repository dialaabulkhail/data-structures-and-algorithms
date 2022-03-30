# Challenge Summary
Create a new class called pseudo queue.
Internally, utilize 2 Stack instances to create and manage the queue.
Methods:
- enqueue --> Inserts value into the PseudoQueue, using a first-in, first-out approach.

- dequeue --> Extracts a value from the PseudoQueue, using a first-in, first-out approach.


## Whiteboard Process
![](./stack-queue-pseudo.jpg)

## Approach & Efficiency
class PseudoQueue: This class is going to utilize 2 Stack instances to create and manage the queue.

**methods:**
enqueue() --> used to push the nodes to the PseudoQueue with first in first out approach.

dequeue() --> extracts a value from the PseudoQueue, using a first-in, first-out approach and returns the extracted value.

**Big O notation of PseudoQueue methods:**
enqueue()--> time complexity O(1)
         --> space complexity O(1)  --> pushes one value at a time 

dequeue() --> time complexity O(n) --> loops through each added value.
          --> space complexity O(1)  --> deletes one value each time.


## Solution
[Code Link](./stack_and_queue/stack_queue_pseudo.py)
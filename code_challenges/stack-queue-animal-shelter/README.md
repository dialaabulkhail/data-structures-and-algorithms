# Challenge Summary
Create a class called AnimalShelter which holds only dogs and cats.
it should follow the first in first out approach.
the class should have two methods of:

- enqueue: Arguments: animal, animal can be either a dog or a cat object.

- dequeue: Arguments: pref, pref can be either "dog" or "cat". Return: either a dog or a cat, based on preference. If pref is not "dog" or "cat" then return null.

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
The approach used was first in first out-last in last out, I used two Queue class objects one for dogs and the other for cats and I used in them the basic enqueue and dequeue from Queue class so it matches the approach of first in first out.

-Two new methods were declared : 
enqueue() --> time complexity is O(1)
          --> space complexity is O(1)

dequeue() --> time complexity is O(1)
          --> space complexity is O(1)

## Solution
[Link of code](./stack_queue_animal_shelter/animanl_shelter.py)
[Link of tests](./tests/test_stack_queue_animal_shelter.py)

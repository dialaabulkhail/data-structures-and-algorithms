import pytest
from linked_list.linked_list import LinkedList

linkedlist = LinkedList()
values = [1,3,2,4,5]   #[5,4,2,3,1]
for value in values:
    linkedlist.insert(value)
    linkedlist.length()


"""
Where k is greater than the length of the linked list
"""
def test_k_greater_than_length():
    assert "Value is out of range!" == linkedlist.kthFromEnd(10)


"""
Where k and the length of the list are the same
"""
def test_k_equals_length():
    assert "Value is out of range!" == linkedlist.kthFromEnd(linkedlist.length())


"""
Where k is not a positive integer
"""
## test of negative is changed to be an exception
def test_negative_k():
    with pytest.raises(Exception):
        linkedlist.kthFromEnd(-2)
        linkedlist.kthFromEnd(-99)


"""
new linked list with size one
"""
size_one_list = LinkedList()
nodes = [110]
for i in nodes:
    size_one_list.insert(i)
    size_one_list.length()

"""
Where the linked list is of a size 1
"""
def test_list_size_one():
    assert "Value is out of range!" == size_one_list.kthFromEnd(size_one_list.length() == 1)
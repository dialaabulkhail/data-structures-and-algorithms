from linked_list.linked_list import LinkedList,Node


###### Code challenge 6 tests (Insertions)##########
linkedlist = LinkedList()
values = [1,3,2]
for value in values:
    linkedlist.insert(value)


def test_append():
    assert "2 -> 3 -> 1 -> 5 -> NULL" == linkedlist.append(5)


def test_insert_before():
    assert "2 -> 5 -> 3 -> 1 -> NULL" == linkedlist.insert_before(3,5)
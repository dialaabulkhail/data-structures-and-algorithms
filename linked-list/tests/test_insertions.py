from linked_list.linked_list import LinkedList,Node



###### Code challenge 6 tests (Insertions)##########
linkedlist = LinkedList()
values = [1,3,2]
for value in values:
    linkedlist.insert(value)


def test_append():
    assert "2 -> 3 -> 1 -> 5 -> NULL" == linkedlist.append(5)



def test_append_to_last():
    linkedlist = LinkedList()
    assert "1 -> NULL" == linkedlist.append(1)



def test_insert_before():
    assert "2 -> 5 -> 3 -> 1 -> 5 -> NULL" == linkedlist.insert_before(3,5)



def test_insert_before_out_of_list():
    assert "Invalid value" == linkedlist.insert_before(10, 5)



def test_insert_after():
    assert "2 -> 5 -> 3 -> 5 -> 1 -> 5 -> NULL" == linkedlist.insert_after(3,5)



def test_insert_after_out_of_list():
    assert "Invalid value" == linkedlist.insert_after(10, 5)
from linked_list.linked_list import LinkedList,Node




def test_empty_linkedlist():
    linkedlist = LinkedList()
    expected = None
    actual = linkedlist.head
    
    assert expected == actual



def test_insert_into_linkedlist():
    linkedlist = LinkedList()
    value = "Inserted"
    linkedlist.insert(value)
    assert linkedlist.head.value == "Inserted"



def test_head_to_first():
    linkedlist = LinkedList()
    linkedlist.insert("first")
    assert linkedlist.head.value == "first"
    linkedlist.insert("second")
    assert linkedlist.head.value == "second"
    linkedlist.insert("third")
    assert linkedlist.head.value == "third"
    assert linkedlist.head.next.value == "second"


"""
To test the includes method we should create a list that takes all nodes coming from insert method
"""
linkedlist = LinkedList()
nodes = ["one", 1, "two", 2]
for i in nodes:
    linkedlist.insert(i)


def test_if_value_included():
    assert linkedlist.includes(1) == True
    assert linkedlist.includes("two") == True
    assert linkedlist.includes("one") == True



def test_if_value_not_included():
    assert linkedlist.includes("hello") == False
    assert linkedlist.includes(99) == False
    assert linkedlist.includes([]) == False
    


def test_str():
    assert linkedlist.__str__() == "2 -> two -> 1 -> one -> NULL"
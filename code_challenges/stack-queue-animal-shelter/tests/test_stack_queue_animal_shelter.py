from stack_queue_animal_shelter.animanl_shelter import AnimalShelter, Queue
import pytest


def test_Queue():
    q = Queue()
    q.enqueue1(1)
    q.enqueue1(2)
    q.enqueue1(3)

    assert 1 == q.front.value
    assert 1 == q.dequeue1()


def test_enqueue_cat():
    q = AnimalShelter()
    q.enqueue("cat")
    q.enqueue("cat")
    assert "cat" == q.cat_queue.front.value
    assert "cat" == q.cat_queue.rear.value


def test_enqueue_dog():
    q = AnimalShelter()
    q.enqueue("dog")
    assert "dog" == q.dog_queue.front.value


def test_dequeue_cat():
    q = AnimalShelter()
    q.enqueue("cat")
    q.enqueue("dog")

    q.dequeue("cat")
    assert "cat" == q.cat_queue.dequeue1()


def test_multiple_dog_dequeue():
    q = AnimalShelter()
    q.enqueue("cat")
    q.enqueue("dog")
    q.enqueue("dog")
    q.enqueue("dog")
    
    assert "dog" == q.dog_queue.dequeue1()
    assert "dog" == q.dog_queue.dequeue1()
    assert "dog" == q.dog_queue.dequeue1()

    with pytest.raises(Exception):
        q.dog_queue.dequeue1()
 

def test_multiple_cat_dequeue():
    q = AnimalShelter()
    q.enqueue("cat")
    q.enqueue("cat")
    q.enqueue("dog")
    q.enqueue("dog")
    
    assert "cat" == q.cat_queue.dequeue1()
    assert "cat" == q.cat_queue.dequeue1()

    with pytest.raises(Exception):
        q.cat_queue.dequeue1()


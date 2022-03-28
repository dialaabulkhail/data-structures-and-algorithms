from logging import raiseExceptions
import pyexpat
from re import L
from stack_and_queue.stack_and_queue import Stack, Queue
import pytest


                                               ## STACK TESTS ## 
## Push tests
def test_push(stack, second_stack):
    assert 4 == stack.top.value
    assert 18 == second_stack.top.value


def test_multiple_push():
    stack = Stack()
    values = [1,2,3,4,5,6,7,8,9,10]
    for i in values:
        stack.push(i)
    assert 10 == stack.top.value


## Pop tests
def test_pop(stack, second_stack):
    assert 4 == stack.pop()
    assert 18 == second_stack.pop()


def test_multiple_pop(stack):
    assert 4 == stack.pop()
    assert 3 == stack.pop()
    assert 2 == stack.pop()
    assert 1 == stack.pop()
    with pytest.raises(Exception):
        stack.pop()


def test_pop_empty_stack():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()


## peek tests
def test_peek(stack, second_stack):
    assert 4 == stack.peek()
    assert 18 == second_stack.peek()


def test_peek_empty_stack():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()


## is_empty tests
def test_stack_is_empty():
    stack = Stack()
    assert True == stack.is_empty()


def test_stack_is_not_empty(stack, second_stack):
    assert False == stack.is_empty()
    assert False == second_stack.is_empty()
    


## Stack Fixturs
@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    return stack

@pytest.fixture
def second_stack():
    stack = Stack()
    stack.push(15)
    stack.push(16)
    stack.push(17)
    stack.push(18)

    return stack 


                                               ## QUEUE TESTS ## 

# enqueue tests
def test_enqueue(queue):
    assert 10 == queue.front.value
    assert 10000 == queue.rear.value


def test_multiple_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    assert 3 == queue.rear.value
    assert 1 == queue.front.value
    queue.enqueue(15)
    assert 15 == queue.rear.value


def test_enqueue_to_empty_queue():
    queue = Queue()
    queue.enqueue(1)
    assert 1 == queue.rear.value
    assert 1 == queue.front.value


## dequeue tests
def test_dequeue(queue):
    assert 10 == queue.dequeue()
    assert 100 == queue.front.value
    assert 1000 == queue.front.next.value


def test_dequeue_of_empty_queue():
    queue = Queue()
    with pytest.raises(Exception):
        queue.dequeue()

    
def test_dequeue_until_empty(queue):
    assert 10 == queue.dequeue()
    assert 100 == queue.dequeue()
    assert 1000 == queue.dequeue()
    assert 10000 == queue.dequeue()
    with pytest.raises(Exception):
        queue.dequeue()


## peek tests
def test__queue_peek(queue):
    assert 10 == queue.peek()


def test_instantiate_empty_queue():
    queue = Queue()
    assert None == queue.front
    assert None == queue.rear


## Queue fictures
@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(100)
    queue.enqueue(1000)
    queue.enqueue(10000)

    return queue

from stack_and_queue.stack_queue_pseudo import PseudoQueue, Stack
import pytest



def test_stack_s(stack):
    q = PseudoQueue(stack)
    assert 10000 == q.s2.peek()
    with pytest.raises(Exception):
        q.s1.peek()


def test_enqueue(stack):
    q = PseudoQueue(stack)
    q.enqueue(5)
    assert 5 == q.s2.peek()


def test_dequeue(stack):
    q = PseudoQueue(stack)
    assert 10 == q.dequeue()


def test_enqueue_dequeue(stack):
    q = PseudoQueue(stack)
    assert 10000 == q.s2.peek()
    q.enqueue("hello")
    assert "hello" == q.s2.peek()
    q.enqueue(55)
    assert 55 == q.s2.peek()



#fixtures
@pytest.fixture
def stack():
    stack = Stack()
    stack.push(10)
    stack.push(100)
    stack.push(1000)
    stack.push(10000)
    
    return stack
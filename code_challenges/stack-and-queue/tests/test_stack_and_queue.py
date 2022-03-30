from stack_and_queue.stack_queue_pseudo import PseudoQueue, Stack
import pytest



def test_stack_new_stack(stack):
    q = PseudoQueue(stack)
    assert 10000 == q.stack.peek()  #top value of stack "last in"
    with pytest.raises(Exception):
        q.new_stack.peek()          # new stack is empty



def test_enqueue(stack):
    q = PseudoQueue(stack)
    assert 10000 == q.stack.peek()  # last enqeueu is the top of stack
    q.enqueue("hello")              # last enqeueu is the top of stack
    assert "hello" == q.stack.peek()
    q.enqueue(55)
    assert 55 == q.stack.peek()



def test_dequeue(stack):
    q = PseudoQueue(stack)
    assert 10 == q.dequeue()   # popped out value of new_stack "top of new stack" first enqueue frist dequeue



def test_pseudoqueue(stack2):
    queue = PseudoQueue(stack2)
    queue.enqueue("happy")  #first enqueue first dequeue
    assert "happy" == queue.dequeue()



def test_empty_dequeue():
    stack = Stack()              # empty stack dequeue
    with pytest.raises(Exception):
        stack.dequeue()



def test_empty_enqueue():         
    stack = Stack()              # top value enqueue while empty
    with pytest.raises(Exception):
        stack.top.value()




#fixtures
@pytest.fixture
def stack():
    stack = Stack()
    stack.push(10)
    stack.push(100)
    stack.push(1000)
    stack.push(10000)   # [10000->1000->100->10] regular stack
                        # [10 -> 100 -> 1000 -> 10000]
    return stack


@pytest.fixture
def stack2():
    s = Stack()
    s.push("happy")  # ["time"->"the"->"all"->"happy"]
    s.push("all")    # ["happy"->"all"->"the"->"time"]
    s.push("the")    
    s.push("time")

    return s

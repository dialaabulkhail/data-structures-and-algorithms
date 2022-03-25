from stack_and_queue.stack_and_queue import Stack, Node
import pytest


def test_push(stack):
    actual = stack.top.value
    expected = 4
    assert actual == expected


def test_pop(stack):
    actual = stack.pop()
    expected = 4
    assert actual == expected



@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    return stack


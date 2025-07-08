from leetcode.stack.min_stack import MinStack


def test_min_stack() -> None:
    stack = MinStack()
    assert stack.push(-2) is None
    assert stack.push(0) is None
    assert stack.push(-3) is None
    assert stack.getMin() == -3
    assert stack.pop() is None
    assert stack.top() == 0
    assert stack.getMin() == -2


def test_min_stack_2() -> None:
    stack = MinStack()
    assert stack.push(2) is None
    assert stack.push(0) is None
    assert stack.push(3) is None
    assert stack.push(0) is None
    assert stack.getMin() == 0
    assert stack.pop() is None
    assert stack.getMin() == 0
    assert stack.pop() is None
    assert stack.getMin() == 0
    assert stack.pop() is None
    assert stack.getMin() == 2

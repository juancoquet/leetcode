# https://leetcode.com/problems/min-stack/description/


class MinStack:
    def __init__(self) -> None:
        self._stack: list[int] = []
        self._min_history: list[int] = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._min_history or val <= self._min_history[-1]:
            self._min_history.append(val)

    def pop(self) -> None:
        if self._stack.pop(-1) == self._min_history[-1]:
            self._min_history.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_history[-1]

# https://leetcode.com/problems/min-stack/description/


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min == [] or val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min[-1]:
            self.min.pop()
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

# https://leetcode.com/problems/valid-parentheses/


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()

        opens = "({["
        matches = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in opens:
                stack.push(ch)
            else:
                top = stack.pop()
                if top != matches[ch]:
                    return False
        return stack.length == 0


class Stack:
    def __init__(self):
        self._stack = []

    @property
    def length(self):
        return len(self._stack)

    def pop(self):
        try:
            top = self._stack.pop()
        except IndexError:
            top = None
        return top

    def push(self, item):
        self._stack.append(item)

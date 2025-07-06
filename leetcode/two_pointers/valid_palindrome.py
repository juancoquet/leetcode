class Solution:
    def isPalindrome(self, s: str) -> bool:
        return simple_solution(norm(s))


def norm(s: str) -> str:
    return "".join(c.lower() for c in s if c.isalnum())


def simple_solution(s: str) -> bool:
    return s == "".join(reversed(s))


def two_pointers_solution(s: str) -> bool:
    for lft, c in enumerate(s):
        rgt = len(s) - 1 - lft
        if lft >= rgt:
            return True
        if c != s[rgt]:
            return False
    return True

import pytest

from leetcode.two_pointers.valid_palindrome import Solution


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ],
)
def test_valid_palindrome(s: str, expected: bool) -> None:
    res = Solution().isPalindrome(s)
    assert res == expected

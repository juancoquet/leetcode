import pytest

from leetcode.sliding_window.longest_substring_without_repeating_characters import Solution


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("au", 2),
        ("aab", 2),
        ("dvdf", 3),
        ("ggububgvfk", 6),
    ],
)
def test_length_of_longest_substring(s: str, expected: int) -> None:
    res = Solution().lengthOfLongestSubstring(s)
    assert res == expected
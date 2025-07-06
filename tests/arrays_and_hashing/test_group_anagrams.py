import pytest

from leetcode.arrays_and_hashing.group_anagrams import Solution


@pytest.mark.parametrize(
    ("inputs", "expected"),
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_group_anagrams(inputs: list[str], expected: list[list[str]]) -> None:
    res = Solution().groupAnagrams(inputs)
    assert equal(expected, res)


def equal(res: list[list[str]], expected: list[list[str]]) -> bool:
    """Compare `res` and `expected` equality regardless of member order"""
    return sorted([sorted(r) for r in res]) == sorted([sorted(e) for e in expected])

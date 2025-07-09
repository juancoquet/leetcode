import pytest

from leetcode.binary_search.binary_search import Solution


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ],
)
def test_binary_search(nums: list[int], target: int, expected: int) -> None:
    solution = Solution()
    assert solution.search(nums, target) == expected
